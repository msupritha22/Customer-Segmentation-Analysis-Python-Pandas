# ============================================================
# Customer Segmentation Analysis | Python + Pandas
# Author: Supritha | Business Analytics Portfolio
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

os.makedirs("outputs", exist_ok=True)

COLORS = ["#2563EB", "#7C3AED", "#059669", "#DC2626",
          "#D97706", "#0891B2", "#9333EA", "#16A34A",
          "#db2777", "#ea580c"]

print("=" * 55)
print("   CUSTOMER SEGMENTATION ANALYSIS")
print("=" * 55)

# ── 1. Load ───────────────────────────────────────────────────
df = pd.read_csv("data/customers.csv")
print(f"\n✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# ── 2. Overview ───────────────────────────────────────────────
print("\n── DATA OVERVIEW ──────────────────────────────────────")
print(df.head())
print(f"\nDescriptive Stats:\n{df.describe().round(1)}")

# ── 3. RFM-style Segmentation (Rule-based) ────────────────────
#
#  Recency  → days_since_last_purchase  (lower = better)
#  Frequency→ total_orders              (higher = better)
#  Monetary → total_spent               (higher = better)
#
def segment(row):
    r = row["days_since_last_purchase"]
    f = row["total_orders"]
    m = row["total_spent"]

    if r <= 60 and f >= 30 and m >= 30000:
        return "Champions"
    elif r <= 90 and f >= 15 and m >= 15000:
        return "Loyal Customers"
    elif r <= 180 and f >= 5:
        return "Potential Loyalists"
    elif r > 270 and f <= 5:
        return "At Risk"
    elif r > 300:
        return "Lost Customers"
    else:
        return "Regular Customers"

df["segment"] = df.apply(segment, axis=1)

# ── 4. Segment Summary ────────────────────────────────────────
seg_summary = (df.groupby("segment")
                 .agg(
                     Customer_Count=("customer_id", "count"),
                     Avg_Orders=("total_orders", "mean"),
                     Avg_Spent=("total_spent", "mean"),
                     Avg_Days_Since_Purchase=("days_since_last_purchase", "mean"),
                 )
                 .round(1)
                 .sort_values("Avg_Spent", ascending=False)
                 .reset_index())

print("\n── SEGMENT SUMMARY ────────────────────────────────────")
print(seg_summary.to_string(index=False))

# ── 5. Membership Tier Distribution ──────────────────────────
tier_count = df["membership_tier"].value_counts().reset_index()
tier_count.columns = ["Tier", "Count"]
print("\n── MEMBERSHIP TIER DISTRIBUTION ───────────────────────")
print(tier_count.to_string(index=False))

# ── 6. Platform Usage ────────────────────────────────────────
platform_rev = (df.groupby("platform")
                  .agg(Customers=("customer_id","count"),
                       Total_Spent=("total_spent","sum"))
                  .reset_index())
print("\n── PLATFORM ANALYSIS ──────────────────────────────────")
print(platform_rev.to_string(index=False))

# ── 7. Age Group Analysis ────────────────────────────────────
bins   = [17, 24, 34, 44, 54, 65]
labels = ["18–24", "25–34", "35–44", "45–54", "55–64"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

age_analysis = (df.groupby("age_group", observed=True)
                  .agg(Count=("customer_id","count"),
                       Avg_Spent=("total_spent","mean"),
                       Avg_Orders=("total_orders","mean"))
                  .round(1)
                  .reset_index())
print("\n── AGE GROUP ANALYSIS ─────────────────────────────────")
print(age_analysis.to_string(index=False))

# ── 8. City-wise Spend ───────────────────────────────────────
city_data = (df.groupby("city")
               .agg(Customers=("customer_id","count"),
                    Avg_Spent=("total_spent","mean"))
               .sort_values("Avg_Spent", ascending=False)
               .reset_index())

# ── 9. Save Outputs ──────────────────────────────────────────
seg_summary.to_csv("outputs/segment_summary.csv", index=False)
df[["customer_id","segment","total_spent","total_orders",
    "days_since_last_purchase"]].to_csv("outputs/customer_segments.csv", index=False)
print("\n✅ CSVs saved to outputs/")

# ── 10. Dashboard ────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("Customer Segmentation Dashboard", fontsize=18,
             fontweight="bold", color="#1e293b", y=1.01)
fig.patch.set_facecolor("#f8fafc")
for ax in axes.flat:
    ax.set_facecolor("#ffffff")

seg_colors = [COLORS[i % len(COLORS)] for i in range(len(seg_summary))]

# Chart 1 – Segment Distribution (donut)
ax1 = axes[0, 0]
wedges, texts, autotexts = ax1.pie(
    seg_summary["Customer_Count"],
    labels=seg_summary["segment"],
    autopct="%1.1f%%",
    colors=seg_colors,
    startangle=140,
    pctdistance=0.80,
    wedgeprops={"edgecolor": "white", "linewidth": 2},
)
for t in autotexts:
    t.set_fontsize(8)
# Donut hole
centre = plt.Circle((0, 0), 0.55, fc="white")
ax1.add_patch(centre)
ax1.set_title("Customer Segments", fontsize=13, fontweight="bold", pad=10)

# Chart 2 – Avg Spend per Segment (bar)
ax2 = axes[0, 1]
bars = ax2.bar(seg_summary["segment"], seg_summary["Avg_Spent"],
               color=seg_colors, edgecolor="white", width=0.6)
ax2.set_title("Avg Spend by Segment (₹)", fontsize=13, fontweight="bold", pad=10)
ax2.set_ylabel("Avg Total Spent (₹)")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"₹{x/1000:.0f}K"))
ax2.tick_params(axis="x", rotation=30)
ax2.grid(axis="y", linestyle="--", alpha=0.4)
for bar in bars:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, h + 200,
             f"₹{h/1000:.0f}K", ha="center", fontsize=8, fontweight="bold")

# Chart 3 – Age Group vs Avg Spent (bar)
ax3 = axes[1, 0]
ax3.bar(age_analysis["age_group"].astype(str),
        age_analysis["Avg_Spent"],
        color=COLORS[:len(age_analysis)], edgecolor="white", width=0.6)
ax3.set_title("Avg Spend by Age Group (₹)", fontsize=13, fontweight="bold", pad=10)
ax3.set_xlabel("Age Group")
ax3.set_ylabel("Avg Total Spent (₹)")
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"₹{x/1000:.0f}K"))
ax3.grid(axis="y", linestyle="--", alpha=0.4)

# Chart 4 – Membership Tier (horizontal bar)
ax4 = axes[1, 1]
tier_order = ["Platinum", "Gold", "Silver", "Free"]
tier_sorted = tier_count.set_index("Tier").reindex(tier_order).reset_index()
tier_c = ["#7C3AED", "#D97706", "#6B7280", "#2563EB"]
ax4.barh(tier_sorted["Tier"], tier_sorted["Count"],
         color=tier_c, edgecolor="white")
ax4.set_title("Membership Tier Distribution", fontsize=13, fontweight="bold", pad=10)
ax4.set_xlabel("Number of Customers")
for i, v in enumerate(tier_sorted["Count"]):
    ax4.text(v + 3, i, str(v), va="center", fontsize=10, fontweight="bold")
ax4.grid(axis="x", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("outputs/customer_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Dashboard saved → outputs/customer_dashboard.png")
print("\n🎉 Segmentation analysis complete!")
