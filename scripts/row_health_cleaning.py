"""
Row Health Data — Cleaning & Preprocessing Pipeline
=====================================================
Produces three clean DataFrames ready for ingestion into MySQL or BigQuery.

Sheets ingested:
  - customers  (16,338 rows × 8 cols)
  - claims     (49,998 rows × 6 cols)
  - campaigns  (57 rows × 6 cols)

Run:
    python row_health_cleaning.py

Outputs:
    customers_clean.csv
    claims_clean.csv
    campaigns_clean.csv
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────
# 0. INGEST
# ─────────────────────────────────────────────────────────────
FILE = "Row_Health_Data.xlsx"

customers = pd.read_excel(FILE, sheet_name="customers")
claims    = pd.read_excel(FILE, sheet_name="claims")
campaigns = pd.read_excel(FILE, sheet_name="campaigns")

print(f"Loaded  customers : {customers.shape}")
print(f"Loaded  claims    : {claims.shape}")
print(f"Loaded  campaigns : {campaigns.shape}")


# ─────────────────────────────────────────────────────────────
# 1. CUSTOMERS
# ─────────────────────────────────────────────────────────────

# 1a. Standardise NULL-equivalent campaign_id values
#     'unknown' string and actual NaN are both sentinel → unify as None
customers["campaign_id"] = customers["campaign_id"].replace("unknown", None)
# Optional: if you want a visible sentinel instead of NULL, use:
# customers["campaign_id"] = customers["campaign_id"].fillna("UNKNOWN")

# 1b. Strip leading/trailing whitespace from all string columns
str_cols_cust = ["customer_id", "first_name", "last_name",
                 "state", "first_touch", "plan", "campaign_id"]
for col in str_cols_cust:
    customers[col] = customers[col].str.strip()

# 1c. Normalise plan & first_touch to lowercase for consistent encoding
customers["plan"]        = customers["plan"].str.lower()
customers["first_touch"] = customers["first_touch"].str.lower()

# 1d. Cast signup_date: datetime64 → date (drops spurious 00:00:00 time)
customers["signup_date"] = pd.to_datetime(customers["signup_date"]).dt.date

# 1e. Enforce expected dtypes
customers = customers.astype({
    "customer_id" : "string",   # VARCHAR(20) in MySQL / STRING in BigQuery
    "first_name"  : "string",
    "last_name"   : "string",
    "state"       : "string",
    "first_touch" : "string",
    "plan"        : "string",
    "campaign_id" : "string",
})

# 1f. Deduplication guard
pre = len(customers)
customers = customers.drop_duplicates(subset="customer_id")
print(f"\n[customers] Dropped {pre - len(customers)} duplicate customer_id rows")

print(f"[customers] NULL campaign_id : {customers['campaign_id'].isna().sum()} rows")
print(f"[customers] Cleaned shape    : {customers.shape}")


# ─────────────────────────────────────────────────────────────
# 2. CLAIMS
# ─────────────────────────────────────────────────────────────

# 2a. Consolidate near-duplicate claim_category label
#     'Physical Therapy Sessions' → 'Physical Therapy'
claims["claim_category"] = claims["claim_category"].replace(
    "Physical Therapy Sessions", "Physical Therapy"
)

# 2b. Cast claim_date to date only
claims["claim_date"] = pd.to_datetime(claims["claim_date"]).dt.date

# 2c. Round monetary amounts to 2 decimal places
claims["claim_amount"]   = claims["claim_amount"].round(2)
claims["covered_amount"] = claims["covered_amount"].round(2)

# 2d. Flag rows where covered_amount > claim_amount (business logic alert)
#     These are NOT dropped — they need domain review.
#     A boolean flag column lets analysts filter them easily.
claims["covered_exceeds_claim"] = (
    claims["covered_amount"] > claims["claim_amount"]
).astype(bool)
n_exceed = claims["covered_exceeds_claim"].sum()
print(f"\n[claims] covered > claim flagged : {n_exceed} rows  (column: covered_exceeds_claim)")

# 2e. Flag temporal integrity violations: claim_date < customer signup_date
customers_dates = customers[["customer_id", "signup_date"]]
claims_merged = claims.merge(customers_dates, on="customer_id", how="left")
claims["claim_before_signup"] = (
    pd.to_datetime(claims_merged["claim_date"]) <
    pd.to_datetime(claims_merged["signup_date"])
)
n_temporal = claims["claim_before_signup"].sum()
print(f"[claims] claim before signup date : {n_temporal} rows  (column: claim_before_signup)")

# 2f. Enforce dtypes
claims = claims.astype({
    "customer_id"    : "string",
    "claim_id"       : "int64",
    "claim_category" : "string",
})
claims["claim_amount"]   = claims["claim_amount"].astype("float64")
claims["covered_amount"] = claims["covered_amount"].astype("float64")

# 2g. Deduplication guard
pre = len(claims)
claims = claims.drop_duplicates(subset="claim_id")
print(f"[claims] Dropped {pre - len(claims)} duplicate claim_id rows")
print(f"[claims] Cleaned shape : {claims.shape}")


# ─────────────────────────────────────────────────────────────
# 3. CAMPAIGNS
# ─────────────────────────────────────────────────────────────

# 3a. Impute NULL clicks as 0
#     (3 rows with high impressions but no clicks recorded — treat as 0)
n_null_clicks = campaigns["clicks"].isna().sum()
campaigns["clicks"] = campaigns["clicks"].fillna(0)
print(f"\n[campaigns] NULL clicks imputed to 0 : {n_null_clicks} rows")

# 3b. Cast clicks to integer (was float64 due to NaN presence)
campaigns["clicks"] = campaigns["clicks"].astype("int64")

# 3c. Derive click-through rate (CTR) as a useful ingestion-ready metric
campaigns["ctr"] = (
    campaigns["clicks"] / campaigns["impressions"]
).round(6)  # e.g. 0.123456

# 3d. Round cost to 2 decimal places
campaigns["cost"] = campaigns["cost"].round(2)

# 3e. Enforce dtypes
campaigns = campaigns.astype({
    "campaign_id"        : "string",
    "campaign_category"  : "string",
    "campaign_type"      : "string",
})

# 3f. Deduplication guard
pre = len(campaigns)
campaigns = campaigns.drop_duplicates(subset="campaign_id")
print(f"[campaigns] Dropped {pre - len(campaigns)} duplicate campaign_id rows")
print(f"[campaigns] Cleaned shape : {campaigns.shape}")


# ─────────────────────────────────────────────────────────────
# 4. REFERENTIAL INTEGRITY CHECK (post-clean)
# ─────────────────────────────────────────────────────────────
valid_campaigns = set(campaigns["campaign_id"])
orphan_cust = customers[
    customers["campaign_id"].notna() &
    ~customers["campaign_id"].isin(valid_campaigns)
]
print(f"\n[integrity] Customers with unresolvable campaign_id : {len(orphan_cust)}")

valid_customers = set(customers["customer_id"])
orphan_claims = claims[~claims["customer_id"].isin(valid_customers)]
print(f"[integrity] Claims with no matching customer        : {len(orphan_claims)}")


# ─────────────────────────────────────────────────────────────
# 5. EXPORT
# ─────────────────────────────────────────────────────────────
customers.to_csv("customers_clean.csv", index=False)
claims.to_csv("claims_clean.csv", index=False)
campaigns.to_csv("campaigns_clean.csv", index=False)

print("\n✓ Exported: customers_clean.csv, claims_clean.csv, campaigns_clean.csv")


# ─────────────────────────────────────────────────────────────
# 6. TARGET SCHEMA (for reference)
# ─────────────────────────────────────────────────────────────
SCHEMA = """
-- MySQL DDL (BigQuery equivalents in comments)

CREATE TABLE customers (
    customer_id   VARCHAR(20)  NOT NULL PRIMARY KEY,    -- STRING
    first_name    VARCHAR(100),
    last_name     VARCHAR(100),
    state         CHAR(2),
    first_touch   VARCHAR(20),                          -- ENUM('social','referral','email','direct','marketplace')
    plan          VARCHAR(20),                          -- ENUM('bronze','silver','gold','platinum')
    signup_date   DATE         NOT NULL,
    campaign_id   VARCHAR(20)  REFERENCES campaigns(campaign_id)
);

CREATE TABLE campaigns (
    campaign_id        VARCHAR(20)   NOT NULL PRIMARY KEY,  -- STRING
    campaign_category  VARCHAR(100),
    campaign_type      VARCHAR(100),
    cost               DECIMAL(10,2),                       -- NUMERIC
    impressions        INT,                                  -- INT64
    clicks             INT,                                  -- INT64
    ctr                DECIMAL(10,6)                        -- FLOAT64
);

CREATE TABLE claims (
    claim_id               INT          NOT NULL PRIMARY KEY,  -- INT64
    customer_id            VARCHAR(20)  NOT NULL REFERENCES customers(customer_id),
    claim_date             DATE         NOT NULL,
    claim_category         VARCHAR(100),
    claim_amount           DECIMAL(10,2),                      -- NUMERIC
    covered_amount         DECIMAL(10,2),                      -- NUMERIC
    covered_exceeds_claim  BOOLEAN      DEFAULT FALSE,
    claim_before_signup    BOOLEAN      DEFAULT FALSE
);
"""
print(SCHEMA)
