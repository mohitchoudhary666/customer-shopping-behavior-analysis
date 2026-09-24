"""Clean and derive analysis fields for the customer shopping dataset."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "customer_shopping_behavior.csv"
OUTPUT_PATH = ROOT / "customer_shopping_behavior_cleaned.csv"

FREQUENCY_DAYS = {
    "annually": 365,
    "bi-weekly": 14,
    "every 3 months": 90,
    "fortnightly": 14,
    "monthly": 30,
    "quarterly": 90,
    "weekly": 7,
}


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize source columns and derive fields used in the notebook."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

    df["review_rating"] = df.groupby("category")["review_rating"].transform(
        lambda values: values.fillna(values.median())
    )
    df["age_group"] = pd.qcut(
        df["age"],
        q=4,
        labels=["Q1 (youngest)", "Q2", "Q3", "Q4 (oldest)"],
    )
    df["purchase_frequency_days"] = (
        df["frequency_of_purchases"].str.strip().str.lower().map(FREQUENCY_DAYS)
    )
    return df


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    cleaned = preprocess(df)
    cleaned.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned data written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
