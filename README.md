# FDA SaMD Clearance Time Visualization

Interactive D3.js visualization analyzing FDA 510(k) clearance times for Software as a Medical Device (SaMD) products.

**[View Live Visualization →](https://prahlaadr.github.io/samd-clearance-viz/)**

---

## What This Shows

A horizontal lollipop chart displaying the **top 20 SaMD product codes** by clearance volume, sorted by average days to FDA clearance. The visualization reveals significant variation in clearance times across different device categories:

| Insight | Value |
|---------|-------|
| **Fastest Category** | QNP (GI Lesion Detection) — 29 days avg |
| **Slowest Category** | OEB (Medical Image Management) — 285 days avg |
| **Highest Volume** | QIH (Medical Image Management) — 75 devices |
| **Overall Average** | 156 days across 206 SaMD clearances |

### Interactive Features

- **Click any product code** to view all 510(k) submissions for that category on [510k.innolitics.com](https://510k.innolitics.com)
- **Hover over data points** for detailed metrics (avg days, range, device count)
- **Top 5 fastest** categories highlighted in orange

---

## Data Source

- **Source:** FDA 510(k) clearance database via [Innolitics 510(k) Database](https://510k.innolitics.com)
- **Period:** January 2025 – January 2026
- **Filter:** Software as a Medical Device (SaMD) only
- **Total:** 206 clearances across 46 unique product codes

---

## How It Was Built

### Data Processing

Raw FDA data was analyzed using **DuckDB** and validated with **Polars**:

```sql
SELECT
    productcode,
    COUNT(*) as device_count,
    ROUND(AVG(days_to_clearance), 0) as avg_days,
    MIN(days_to_clearance) as min_days,
    MAX(days_to_clearance) as max_days
FROM samd_clearances
WHERE days_to_clearance IS NOT NULL
GROUP BY productcode
ORDER BY device_count DESC
LIMIT 20;
```

### Visualization

Built with **D3.js v7** featuring:

- Horizontal lollipop chart with custom SVG rendering
- Clickable Y-axis labels linking to [510k.innolitics.com](https://510k.innolitics.com)
- Product code descriptions from FDA regulation summaries
- Interactive tooltips with detailed metrics
- Innolitics brand colors (#2D3F86 primary, #E85036 highlight)
- Poppins typography via Google Fonts

### Product Code Categories

| Code | Description |
|------|-------------|
| QNP | Gastrointestinal Lesion Detection |
| QFM, QAS | CAD Triage & Notification |
| POK | CAD for Lesions (Cancer) |
| QJI | Automated Glycemic Controller |
| QIH, LLZ, QKB, OEB | Medical Image Management |
| MYN | Medical Image Analyzer |
| QDQ | CAD Detection & Diagnosis |
| MUJ | Radiation Therapy System |
| JAK | Computed Tomography System |
| OLZ, OMB | Electroencephalograph |
| SDJ | Cardiovascular Status Indicator |

---

## Files

| File | Description |
|------|-------------|
| `index.html` | D3.js visualization (standalone, no build required) |
| `clearance_viz.py` | Marimo notebook version with Altair charts |
| `top20_product_codes.json` | Processed data |
| `analysis_summary.md` | Detailed analysis notes |

---

## Run Locally

Just open `index.html` in any browser — no server or build step required.

For the Marimo notebook version:
```bash
marimo run clearance_viz.py
```

---

## Live Demo

**https://prahlaadr.github.io/samd-clearance-viz/**

---

Built by [Innolitics](https://innolitics.com) — Medical Device Software Experts
