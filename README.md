# E-commerce Sales Data Analysis

## Project overview
This beginner-friendly analytics project explores e-commerce orders using Python, Pandas, and Matplotlib. It demonstrates data inspection, data cleaning, KPI calculation, grouped analysis, chart creation, and business recommendations.

**Important:** `data/ecommerce_sales.csv` is synthetic sample data created for practice. It is not real company data and should not be presented as actual business performance.

## Business questions
- What are total revenue, profit, average revenue per order, and profit margin?
- Which product category generates the most revenue?
- Which region generates the most revenue?
- How does revenue change month by month?
- Which products contribute most to revenue?

## Tools
- Python
- Pandas
- Matplotlib
- CSV data

## Run the project
1. Install Python 3.10+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python analysis.py
   ```
4. Check the `outputs/` folder for charts, summary CSV files, and `business_insights.md`.

You can also upload `analysis.py` and the CSV to Google Colab and run the cells there.

## Workflow
1. Load and inspect data.
2. Check missing values and duplicate order IDs.
3. Fill missing text fields and remove duplicate order IDs.
4. Calculate business KPIs.
5. Aggregate revenue by month, category, region, and product.
6. Save charts and tables.
7. Generate business insights and suggested actions.

## Folder structure
```text
ecommerce-sales-analysis/
├── data/
│   └── ecommerce_sales.csv
├── outputs/
│   └── (generated charts, tables, insights)
├── analysis.py
├── requirements.txt
└── README.md
```

## Limitations
- The dataset is synthetic and small.
- The analysis shows correlation and summaries, not causal relationships.
- Real business recommendations require validated, representative data.

## Author
Kaushal R. Shinde
