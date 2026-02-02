# FDA SaMD Clearance Time Visualization

Interactive visualization showing average FDA 510(k) clearance times for the top 20 Software as a Medical Device (SaMD) product codes by volume.

**[View Live Visualization](https://prahlaadr.github.io/samd-clearance-viz/)**

![Lollipop chart showing FDA clearance times by product code](https://img.shields.io/badge/D3.js-Interactive-orange)

## Overview

This visualization analyzes FDA 510(k) clearance data for SaMD devices from January 2025 to January 2026, highlighting:

- **206 total clearances** across 46 unique product codes
- **Top 20 product codes** ranked by clearance volume
- **Average clearance time** ranging from 29 to 285 days

### Key Findings

| Metric | Value |
|--------|-------|
| Fastest Avg Clearance | QNP - 29 days |
| Slowest Avg Clearance | OEB - 285 days |
| Most Clearances | QIH - 75 devices |
| Overall Average | 156 days |

## How It Was Built

### Data Processing

Raw FDA 510(k) clearance data was processed using **DuckDB** and **Polars**:

```python
import polars as pl

# Group by product code, calculate metrics
top20 = (
    df.filter(pl.col("days_to_clearance").is_not_null())
    .group_by("productcode")
    .agg([
        pl.count().alias("device_count"),
        pl.col("days_to_clearance").mean().round(0).alias("avg_days"),
        pl.col("days_to_clearance").min().alias("min_days"),
        pl.col("days_to_clearance").max().alias("max_days"),
    ])
    .sort("device_count", descending=True)
    .head(20)
)
```

### Visualization

Built with **D3.js v7** featuring:

- Horizontal lollipop chart sorted by clearance time
- Interactive hover tooltips with detailed metrics
- Top 5 fastest clearances highlighted in orange
- Innolitics brand colors (#2D3F86, #E85036)
- Poppins typography

### Files

| File | Description |
|------|-------------|
| `index.html` | D3.js visualization (standalone, no build step) |
| `clearance_viz.py` | Marimo notebook version with Altair |
| `top20_product_codes.json` | Processed data |
| `analysis_summary.md` | Detailed analysis notes |

## Run Locally

Just open `index.html` in a browser - no server required.

For the Marimo version:
```bash
marimo run clearance_viz.py
```

## Data Source

FDA 510(k) clearance database, filtered for Software as a Medical Device (SaMD) submissions.

---

Built by [Innolitics](https://innolitics.com)
