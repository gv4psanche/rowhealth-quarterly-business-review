<!-- ![RowHealth Logo](images/RowHealth_Logo_Small.png) -->
<div align="center"><a href="#about-the-project"><img src="images/RowHealth_Logo_Medium.png" width="150" alt="bits&bytes logo" /></a></div>

# <div align="center">Marketing Insights and Recommendation (QBR)</div>

<div align="center">Campaign and Claims Performance</div>

<div align="center"><b>Period:</b> 2019 – 2023 &nbsp;|&nbsp; <b>Team:</b> Data Analytics &nbsp;|&nbsp; <b>Updated:</b> September 2023 &nbsp;|&nbsp; <b>Tools:</b> Excel/Power BI &nbsp;|&nbsp; <a href="#about-the-project">Project Overview</a></div>

---

## Overview

RowHealth is a Houston, TX-based private medical insurance company founded in 2016. This project analyzes three years of customer, campaign, and claims data (2019–2023) to surface Northstar Metrics for two distinct stakeholder audiences — **Marketing Leadership** and **Finance** — and delivers them through an interactive analytics dashboard mockup.

The dataset spans **16,338 members**, **49,998 claims**, and **57 marketing campaigns** across 12 campaign categories, with member enrollment in four plan tiers: Bronze, Silver, Gold, and Platinum.

Now that they’ve hired a new data team and are strategizing their marketing budget for the year, the company would like to build more understanding of the effectiveness of these campaign categories and how they relate to signups and subsequent patient claims. **As a data analyst at Row Health, your focus is on building visualizations** to enable the marketing team to self-serve insights and regular-cadence reporting.

---

## Business Context

In 2019, RowHealth launched a new set of marketing campaign categories covering wellness tips, plan affordability, and preventive care. The core analytical questions driving this project were:

- Which campaigns most efficiently acquire new members?
- Are higher-tier plan members more or less profitable after claims?
- Where are the financial concentration risks in the claims portfolio?
- Can a single bridging metric connect marketing performance to financial outcomes?

---

## Northstar Metrics

### Marketing Leadership
| Metric | Value |
|---|---|
| Total members acquired | 16,338 |
| Top acquisition channel | Social (58%) |
| Total campaign impressions | 9.1M |
| Average CTR across campaigns | 9.4% |
| Best proxy CAC | $0.65 — #CoverageMatters |
| Worst proxy CAC | $176.73 — Golden Years Security |

### Finance
| Metric | Value |
|---|---|
| Total claims billed | $13.4M |
| Total claims covered | $8.2M |
| Overall coverage ratio | 61.2% |
| Highest-risk claim category | Glucose Monitoring (41.7% of all claims) |
| Coverage ratio range by plan | Bronze 50.2% → Platinum 80.0% |

---

## Key Findings

**Marketing**
- Social and referral channels account for 92% of all member signups, yet campaign spend is spread broadly — several low-volume categories carry CAC above $40.
- Only 12 Platinum members exist across the entire member base, suggesting a gap between product offering and campaign messaging for premium plans.
- `Health For All` and `Benefit Updates` achieve the highest CTR (25.5% and 22.2%) despite relatively modest impressions, indicating strong message-market fit.

**Finance**
- Glucose Monitoring alone represents 41.7% of claims by count and 38.8% of total billed dollars — a single-category concentration risk.
- Bronze plan members file the fewest claims per member (1.63) yet receive the worst coverage ratio (50.2%), a potential pricing or retention risk.
- Coverage ratio is nearly identical across all acquisition channels (59.8%–61.8%), meaning channel mix does not materially affect claims liability.

**Bridging metric — Loss ratio by acquisition channel**
> A campaign that brings in high-claim members at low CAC is not a win. The bridging metric connects marketing's cost efficiency directly to finance's coverage exposure, enabling cross-functional budget decisions.

---

## Dashboard

The Power BI mockup is structured across three views:

1. **Marketing Leadership** — member growth trend, channel mix, plan enrollment distribution, proxy CAC ranking, and CTR by campaign category
2. **Finance** — coverage ratio by plan tier, claims per member, claim category concentration, and channel-level loss ratio
3. **Bridging metric** — bubble chart overlays showing CAC vs. coverage ratio and claims-per-member vs. coverage ratio across plan tiers and channels

---

## Data Notes

- CAC is a **proxy only** — derived from campaigns with known spend and matched customer IDs. Campaigns with null spend or unattributed signups (`unknown` campaign ID) are excluded.
- No premium/revenue data is available in the dataset; true loss ratio and LTV calculations are not possible without it.
- Signup dates span 2019–2023, with 2023 figures representing a partial year.

*Bits&Bytes Commerce Inc. · Revenue Analytics · Confidential &nbsp;|&nbsp; `sales-performance-review · v1.2.0`*

<br />

---


## About The Project 

### Company <img src="images/icon_company_small.png" alt="icon company" width="30px" />
**RowHealth is a Houston, Texas-based private health insurance company founded in 2016**, dedicated to making quality healthcare coverage accessible and affordable across the United States. With a team of 250–500 employees, RowHealth has grown to serve over 16,000 members nationwide — with a particularly strong presence in New Jersey, New York, and the broader mid-Atlantic and Midwest regions. Members can choose from four tiered plan offerings — Bronze, Silver, Gold, and Platinum — designed to match a range of healthcare needs and budgets, with the Silver plan being the most widely adopted.

Since 2019, RowHealth has invested heavily in data-driven marketing to expand its reach and member education. Spanning categories such as wellness tips, preventive care, plan comparisons, and affordability messaging, the company's campaigns have generated over 9 million impressions and more than 850,000 clicks — demonstrating strong engagement across digital and social channels. Social media and referrals are the two leading acquisition channels, reflecting the trust RowHealth has built within the communities it serves. The company's campaigns are thoughtfully tailored — ranging from seasonal wellness content to policy information and customer testimonials — reinforcing its commitment to transparency and member empowerment.

On the claims side, RowHealth has processed nearly 50,000 claims totaling over $13 million in billed services, covering approximately 61% of those costs for members. The breadth of covered services — from glucose monitoring and physical therapy to mental health counseling and radiation therapy — underscores RowHealth's commitment to comprehensive, whole-person care. As the company continues to scale, it remains focused on delivering plan flexibility, proactive health engagement, and meaningful coverage to its growing member base.

### The Ask <img src="images/icon_request_small.png" alt="icon requirements" width="30px" />
After their successful 2019 marketing campaign launch, the company has generated over data comprising 9 million impressions and more than 850,000 clicks. The Marketing team is strategizing their marketing budget for the year and would like to build better understanding of the effectiveness of these campaign categories and how they relate to signups and subsequent patient claims. The data team has been asked to build visualizations to enable the marketing team to self-serve insights and regular-cadence reporting:
 
#### Northstar Metrics
* **Customer Acquisition Cost (CAC)** - Measures the total cost of acquiring a new member, helping to assess the efficiency of marketing campaigns.
* **Campaign Conversion Rate** - Clicks → actual signups. Knowing which campaign categories (e.g., Compare Health Coverage vs. Affordable Plans) drive the most enrollments justifies budget allocation.
* **Member Retention Rate** - Indicates the percentage of members who renew their policies, reflecting customer satisfaction and loyalty.
* **Member Growth Rate Over Time** - Signup trends from 2019–2023 reveal whether campaigns are accelerating or plateauing growth.
* **Claims Processing Time** - Tracks the average time taken to process claims, which is crucial for member satisfaction and operational efficiency.
* **Net Promoter Score (NPS)** - Gauges member satisfaction and likelihood to recommend the insurance provider, influencing both retention and acquisition.

### Assumptions  <img src="images/icon_assumptions_small.png" alt="icon assumptions" width="30px" />
* **Backdated Analysis** - This analysis reporting assumes that the present year is 2023 and the data for review is from the prior 4 years of 2019-2022.
* **A 'Proxy' Campaign-level CAC** - Only spend per campaign and not a true company-wide CAC can be calculate given only "cost per campaign" data is available .
* **3rd Assumption** - add more here.

### Operational Data <img src="images/icon_data_small.png" alt="icon data" width="30px" />
**RowHealth’s** current book of business encompasses nearly **16,000 members** and more than **50,000 claims**, yielding a total billed services exceeding **$13M USD**. The accompanying Patient Member dataset provides comprehensive data across multiple dimensions, including patient member information, claims transactions, and campaign program engagement.  

<div align="center">
 <img src="images/rowhealth_ERD_diagram.png" width="450" alt="rowhealth logo" /><br>
 RowHealth Entity Relationship Diagram (ERD)
</div>
<br />

**Note:** <img src="images/icon_assumptions_small.png" alt="icon assumptions" width="20px" /> "*add work here*" dataset. See [EDA process](/doc/RH_EDA.pdf) on how the dataset was cleaned and prepared for this analysis.

<br>
<br>
<div align="center">

[Back to Sales Performance Review](#marketing-insights-and-recommendation-qbr)

</div>
<br>

---

<div align="center">
 <img src="images/RowHealth_Logo_Medium.png" width="100" alt="rowhealth logo" /><br>
</div>
