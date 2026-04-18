# 🛒 Customer Shopping Behavior Analysis

> End-to-end analysis of retail customer purchasing patterns using Python, SQL, and Power BI.

This project digs into a 3,900-record retail dataset to uncover how demographics, seasons, discounts, and subscription status drive purchasing decisions. It covers the full analytics pipeline — data cleaning, exploratory analysis, SQL-based business queries, and an interactive Power BI dashboard — making it a solid reference for anyone learning data analytics.

---

## 📁 Repository Structure

```
customer-shopping-behavior-analysis/
│
├── customer_shopping_behavior.csv             # Raw dataset (3,900 customer transactions)
├── data_preprocessing.py                      # Python script: cleaning & feature engineering
├── customer_shoping_behaviour_analysis.ipynb  # Jupyter notebook: EDA & visualizations
├── customer_behavior_sql_queries.sql          # 10 business-focused SQL queries
├── customer behavior dashboard.pbix           # Interactive Power BI dashboard
│
├── Business Problem Document.pdf              # Project scope and objectives
├── Customer Shopping Behavior Analysis.pdf    # Full written analysis report
│
├── requirements.txt                           # Python dependencies
├── CONTRIBUTING.md                            # Contribution guidelines
└── LICENSE                                    # MIT License
```

---

## 📊 Dataset Overview

**File:** `customer_shopping_behavior.csv`  
**Records:** 3,900 customer transactions

| Column | Description |
|---|---|
| `Customer ID` | Unique identifier for each customer |
| `Age` | Customer age |
| `Gender` | Male / Female |
| `Item Purchased` | Name of the product bought |
| `Category` | Product category (Clothing, Footwear, Accessories, Outerwear) |
| `Purchase Amount (USD)` | Transaction value in USD |
| `Location` | US state of the customer |
| `Size` | Product size (S, M, L, XL) |
| `Color` | Color of the product |
| `Season` | Season of purchase (Spring, Summer, Fall, Winter) |
| `Review Rating` | Customer rating (1.0 – 5.0) |
| `Subscription Status` | Whether the customer has an active subscription (Yes / No) |
| `Shipping Type` | Shipping method (Standard, Express, Free Shipping, etc.) |
| `Discount Applied` | Whether a discount was applied (Yes / No) |
| `Promo Code Used` | Whether a promo code was used (Yes / No) |
| `Previous Purchases` | Number of past purchases by the customer |
| `Payment Method` | Payment method used (Credit Card, PayPal, Venmo, etc.) |
| `Frequency of Purchases` | How often the customer shops (Weekly, Monthly, Quarterly, etc.) |

---

## 🔍 Analysis Highlights

### 🐍 Python Notebook (`customer_shoping_behaviour_analysis.ipynb`)

Exploratory data analysis using `pandas`, `matplotlib`, `seaborn`, and `plotly`:

- Distribution of purchase amounts, age groups, and product categories
- Revenue breakdown by gender, season, and location
- Correlation between review ratings and purchase value
- Discount and promo code usage patterns
- Subscription status vs. spending behavior

### 🗄️ SQL Queries (`customer_behavior_sql_queries.sql`)

10 business-focused queries covering:

| # | Question |
|---|---|
| Q1 | Total revenue by gender |
| Q2 | Discount users who still spend above average |
| Q3 | Top 5 products by average review rating |
| Q4 | Average purchase amount: Standard vs. Express shipping |
| Q5 | Subscriber vs. non-subscriber spend and revenue |
| Q6 | Top 5 products with highest discount usage rate |
| Q7 | Customer segmentation: New / Returning / Loyal |
| Q8 | Top 3 most purchased products per category |
| Q9 | Repeat buyers (5+ purchases) and subscription likelihood |
| Q10 | Revenue contribution by age group |

### 📈 Power BI Dashboard (`customer behavior dashboard.pbix`)

Interactive dashboard with filters for gender, season, and category, featuring:

- Revenue trends and KPIs
- Category and location breakdowns
- Customer segmentation visuals

---

## ⚙️ Getting Started

> **Requirements:** Python 3.8+

### 1. Clone the repository

```bash
git clone https://github.com/mohitchoudhary666/customer-shopping-behavior-analysis.git
cd customer-shopping-behavior-analysis
```

### 2. Set up a virtual environment and install dependencies

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. (Optional) Preprocess the data

```bash
python data_preprocessing.py
```

This cleans the raw dataset and writes a cleaned copy to `customer_shopping_behavior_cleaned.csv`.

### 4. Run the notebook

```bash
jupyter notebook customer_shoping_behaviour_analysis.ipynb
```

Open the notebook in your browser and run the cells to explore the data and visualizations.

### 5. (Optional) Explore SQL queries

Load `customer_shopping_behavior.csv` into a PostgreSQL (or compatible) database and run the queries in `customer_behavior_sql_queries.sql`.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Data processing & EDA |
| pandas, numpy | Data manipulation |
| matplotlib, seaborn, plotly | Visualizations |
| Jupyter Notebook | Interactive analysis |
| SQL (PostgreSQL) | Business queries |
| Power BI | Interactive dashboard |

---

## 🚀 Potential Improvements

- Add a real-world retail dataset (e.g., from Kaggle) to replace synthetic data
- Implement cohort analysis and customer lifetime value (CLV) modelling
- Add a Plotly Dash app for an open-source interactive dashboard
- Set up automated data validation and CI for the preprocessing pipeline

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is released under the [MIT License](LICENSE).
