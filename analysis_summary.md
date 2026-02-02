# SaMD FDA Clearance Data Analysis

## Dataset Overview

| Metric | Value |
|--------|-------|
| Total Records | 206 |
| Unique Product Codes | 46 |
| Date Range | Feb 2024 - Dec 2025 |
| Overall Average Days to Clearance | 156.1 days |

## Top 20 Product Codes by Clearance Volume

| Rank | Product Code | Device Count | Avg Days | Min Days | Max Days |
|------|--------------|--------------|----------|----------|----------|
| 1 | QIH | 75 | 156 | 22 | 273 |
| 2 | QAS | 14 | 91 | 18 | 192 |
| 3 | MYN | 14 | 207 | 103 | 282 |
| 4 | LLZ | 13 | 149 | 22 | 271 |
| 5 | QKB | 6 | 156 | 27 | 266 |
| 6 | MUJ | 6 | 207 | 91 | 420 |
| 7 | JAK | 5 | 170 | 111 | 212 |
| 8 | POK | 5 | 106 | 25 | 158 |
| 9 | QDQ | 5 | 200 | 54 | 279 |
| 10 | QJI | 4 | 130 | 68 | 249 |
| 11 | QNP | 4 | 29 | 28 | 32 |
| 12 | OLZ | 3 | 153 | 90 | 254 |
| 13 | QFM | 3 | 87 | 35 | 126 |
| 14 | QYE | 3 | 175 | 146 | 199 |
| 15 | OEB | 3 | 285 | 184 | 443 |
| 16 | SDJ | 2 | 153 | 150 | 155 |
| 17 | QHA | 2 | 145 | 119 | 170 |
| 18 | QJU | 2 | 155 | 110 | 199 |
| 19 | OMB | 2 | 135 | 126 | 143 |
| 20 | QWO | 2 | 163 | 130 | 196 |

## Key Insights

### Fastest Clearances (Top 5)
1. **QNP** - 29 days avg (n=4) - remarkably consistent (28-32 day range)
2. **QFM** - 87 days avg (n=3)
3. **QAS** - 91 days avg (n=14)
4. **POK** - 106 days avg (n=5)
5. **QJI** - 130 days avg (n=4)

### Slowest Clearances (Top 5)
1. **OEB** - 285 days avg (n=3) - also has widest range (184-443 days)
2. **MYN** - 207 days avg (n=14)
3. **MUJ** - 207 days avg (n=6)
4. **QDQ** - 200 days avg (n=5)
5. **QYE** - 175 days avg (n=3)

### Volume Leaders
- **QIH** dominates with 75 clearances (36% of total dataset)
- Next tier: QAS, MYN, LLZ (13-14 each)
- Long tail: most codes have 2-6 clearances

## Data Files

- `top20_product_codes.json` - Processed data for D3.js visualization
- `index.html` - Interactive lollipop chart visualization
