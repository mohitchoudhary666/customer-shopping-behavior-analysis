# Customer Shopping Behavior Analysis

A Python, SQL, and Power BI analysis project using a synthetic customer-shopping dataset. It includes a Jupyter notebook, preprocessing script, SQL examples, a Power BI file, and report PDFs.

## Repository files

- `customer_shopping_behavior.csv`: source dataset
- `customer_shoping_behaviour_analysis.ipynb`: exploratory analysis and PostgreSQL load example
- `data_preprocessing.py`: date parsing, text cleanup, and year/month features
- `customer_behavior_sql_queries.sql`: example customer and product analyses
- `customer behavior dashboard.pbix`: Power BI dashboard
- `Customer Shopping Behavior Analysis.pdf`: project report
- `Business Problem  Document.pdf`: business problem document

## Run the preprocessing script

Requirements: Python 3 and the packages in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
python data_preprocessing.py
```

The script writes `customer_shopping_behavior_cleaned.csv` beside the source file.

## Run the notebook

Open `customer_shoping_behaviour_analysis.ipynb` in Jupyter and run the cells from top to bottom. The PostgreSQL import cell reads the connection string from the `DATABASE_URL` environment variable; set it locally before running that cell. Do not put credentials in the notebook.

The dataset is synthetic, so its patterns should be treated as practice analysis rather than evidence about real customer behavior.
