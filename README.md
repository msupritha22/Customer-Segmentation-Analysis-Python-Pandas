# Customer-Segmentation-Analysis-Python-Pandas
> A Python project that segments 500 e-commerce customers using RFM logic (Recency, Frequency, Monetary) and visualises behaviour patterns across age groups, cities, and membership tiers.

---

##  Project Overview

This project applies **rule-based RFM segmentation** on a simulated Indian e-commerce customer dataset. It identifies Champions, Loyal Customers, At-Risk users, and more — then delivers a clean 4-chart dashboard.

---

##  Segments Defined

| Segment | Criteria |
|---------|---------|
|  Champions | Recent buyers, high frequency & spend |
|  Loyal Customers | Regular buyers, solid spend |
|  Potential Loyalists | Active but not yet high-value |
|  At Risk | Haven't bought recently, low orders |
|  Lost Customers | Very inactive customers |
|  Regular Customers | Everyone else |

---

##  Analysis Performed

- RFM-style customer segmentation (rule-based)
- Average spend & orders per segment
- Age group spending behaviour (18–24 to 55–64)
- Membership tier distribution (Free / Silver / Gold / Platinum)
- City-wise average spend
- Platform analysis (App vs Website)

---

##  Project Structure

```
customer_segmentation/
│
├── data/
│   └── customers.csv              # Auto-generated (500 customers)
│
├── outputs/
│   ├── customer_dashboard.png     # 2×2 visualisation dashboard
│   ├── segment_summary.csv        # Summary per segment
│   └── customer_segments.csv      # Each customer's segment label
│
├── generate_data.py               # Step 1 — Creates dataset
├── customer_segmentation.py       # Step 2 — Full analysis
├── requirements.txt
└── README.md
```

---

##  How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/customer-segmentation.git
cd customer-segmentation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python generate_data.py

# 4. Run segmentation analysis
python customer_segmentation.py
```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Pandas | Data wrangling & aggregation |
| Matplotlib | Dashboard visualisation |
| NumPy | Data generation |

---

##  Dataset Columns

| Column | Description |
|--------|-------------|
| `customer_id` | Unique customer ID |
| `age` | Customer age (18–64) |
| `gender` | Male / Female / Other |
| `city` | Indian city |
| `total_orders` | Lifetime order count |
| `total_spent` | Lifetime spend (₹) |
| `avg_order_value` | Spend ÷ Orders |
| `days_since_last_purchase` | Recency in days |
| `platform` | App or Website |
| `membership_tier` | Free / Silver / Gold / Platinum |
| `avg_rating_given` | Customer satisfaction rating |

---

##  Business Insights

- **Champions** should receive loyalty rewards and early-access deals
- **At-Risk customers** need win-back campaigns (discount coupons, push notifications)
- **25–34 age group** typically shows the highest average spend — prime marketing target
- **App users** tend to order more frequently than website users

---

<img width="875" height="622" alt="image" src="https://github.com/user-attachments/assets/5e3551ef-9acb-4c30-82fb-a51f8df3adf3" />

## 👩‍💻 Author

**Supritha** — MBA (Business Analytics) | IFIM Business School, Bengaluru  
🔗 [LinkedIn](#) | 💻 [GitHub](#)
