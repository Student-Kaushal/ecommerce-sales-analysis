"""
E-commerce Sales Analysis
Dataset: synthetic sample data created for learning/demo purposes.
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "ecommerce_sales.csv"
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(exist_ok=True)

# 1) Load data
df = pd.read_csv(DATA_PATH)
print("\n=== DATA PREVIEW ===")
print(df.head())
print("\nRows and columns:", df.shape)
print("\nMissing values before cleaning:\n", df.isna().sum())
print("Duplicate order IDs before cleaning:", df["Order_ID"].duplicated().sum())

# 2) Clean data
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Region"] = df["Region"].fillna("Unknown")
df["Product"] = df["Product"].fillna("Unknown Product")
df = df.drop_duplicates(subset=["Order_ID"], keep="first")
df = df.dropna(subset=["Order_Date", "Revenue", "Profit"])
print("\nRows after cleaning:", len(df))

# 3) Key performance indicators (KPIs)
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders if total_orders else 0
profit_margin = (total_profit / total_revenue * 100) if total_revenue else 0

print("\n=== BUSINESS KPIs ===")
print(f"Total revenue: ₹{total_revenue:,.2f}")
print(f"Total profit: ₹{total_profit:,.2f}")
print(f"Unique orders: {total_orders}")
print(f"Average revenue per order: ₹{average_order_value:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")

# 4) Grouped analysis
monthly = df.assign(Month=df["Order_Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["Revenue"].sum()
category = df.groupby("Category", as_index=False).agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum"), Quantity=("Quantity", "sum")).sort_values("Revenue", ascending=False)
region = df.groupby("Region", as_index=False).agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum")).sort_values("Revenue", ascending=False)
product = df.groupby("Product", as_index=False).agg(Revenue=("Revenue", "sum"), Quantity=("Quantity", "sum")).sort_values("Revenue", ascending=False).head(10)

monthly.to_csv(OUT_DIR / "monthly_revenue.csv", index=False)
category.to_csv(OUT_DIR / "category_performance.csv", index=False)
region.to_csv(OUT_DIR / "regional_performance.csv", index=False)
product.to_csv(OUT_DIR / "top_10_products.csv", index=False)

# 5) Visualizations
plt.figure(figsize=(11, 5))
plt.plot(monthly["Month"], monthly["Revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(category["Category"], category["Revenue"])
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUT_DIR / "category_revenue.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(region["Region"], region["Revenue"])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig(OUT_DIR / "regional_revenue.png", dpi=150)
plt.close()

# 6) Evidence-based insights generated from this dataset
best_category = category.iloc[0]
best_region = region.iloc[0]
best_product = product.iloc[0] if not product.empty else None
best_month = monthly.loc[monthly["Revenue"].idxmax()] if not monthly.empty else None

insights = [
    "# Business Insights",
    "",
    "> These insights are calculated from the included synthetic sample dataset. Replace it with real, authorized data before making real business decisions.",
    "",
    f"- Total revenue is **₹{total_revenue:,.2f}** across **{total_orders} unique orders**.",
    f"- Total profit is **₹{total_profit:,.2f}**, with a profit margin of **{profit_margin:.2f}%**.",
    f"- Highest-revenue category: **{best_category['Category']}** (₹{best_category['Revenue']:,.2f}).",
    f"- Highest-revenue region: **{best_region['Region']}** (₹{best_region['Revenue']:,.2f}).",
]
if best_product is not None:
    insights.append(f"- Top product by revenue among the top-10 list: **{best_product['Product']}** (₹{best_product['Revenue']:,.2f}).")
if best_month is not None:
    insights.append(f"- Best month by revenue: **{best_month['Month']}** (₹{best_month['Revenue']:,.2f}).")
insights += [
    "",
    "## Suggested business actions",
    "- Investigate why the leading category performs well and check whether its margin is also strong.",
    "- Compare regional revenue with profit before increasing regional marketing spend.",
    "- Review the monthly trend to plan inventory and promotions around stronger periods.",
    "- Validate these patterns against a larger real-world dataset before taking action."
]
(OUT_DIR / "business_insights.md").write_text("\n".join(insights), encoding="utf-8")

print("\n=== CATEGORY PERFORMANCE ===\n", category.to_string(index=False))
print("\n=== REGIONAL PERFORMANCE ===\n", region.to_string(index=False))
print("\nSaved charts and summary tables in the 'outputs' folder.")
print("Open outputs/business_insights.md for the automatically generated insights.")
