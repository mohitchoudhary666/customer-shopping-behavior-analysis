# Customer Shopping Behavior Analysis

Exploratory analysis of 3,900 customer shopping records using Python, SQL, and Power BI. The included CSV has customer, product, purchase amount, subscription, shipping, discount, and purchase-frequency fields. It has no transaction date, so it supports cross-sectional comparisons rather than time-series or cohort analysis.

## Repository files

- `customer_shopping_behavior.csv`: source dataset (3,900 rows)
- `customer_shoping_behaviour_analysis.ipynb`: exploratory analysis, feature engineering, example PostgreSQL load
- `data_preprocessing.py`: reusable cleaning and feature engineering
- `customer_behavior_sql_queries.sql`: example customer and product questions
- `customer behavior dashboard.pbix`: Power BI dashboard
- `Customer Shopping Behavior Analysis.pdf`: project report
- `Business Problem  Document.pdf`: business problem document

## Run the preprocessing script

Requirements: Python 3 and the packages in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
python data_preprocessing.py
```

This writes `customer_shopping_behavior_cleaned.csv` beside the source file.

## Run the notebook

Open `customer_shoping_behaviour_analysis.ipynb` in Jupyter and run the analysis cells in order. The PostgreSQL import cell expects a local `DATABASE_URL` environment variable; set it in your environment before running that cell. Do not store database credentials in the notebook.

The SQL examples expect a table named `customer`, matching the notebook's PostgreSQL import cell. The Power BI file is provided separately.

## Analysis scope

The notebook fills missing review ratings by product category, standardizes column names, creates age quartiles and maps purchase frequency labels to approximate day intervals. SQL examples compare purchase amounts, discounts, shipping types, subscriptions, and product activity.

The dataset is synthetic. Interpret its patterns as practice analysis, not as evidence about real customers.
