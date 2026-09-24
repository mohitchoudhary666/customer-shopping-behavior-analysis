"""Data preprocessing for the customer shopping behavior dataset."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "customer_shopping_behavior.csv"
OUTPUT_PATH = ROOT / "customer_shopping_behavior_cleaned.csv"


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic cleaning and feature engineering."""
    df = df.copy()
    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
    df["gender"] = df["gender"].str.upper().str.strip()
    df["payment_method"] = df["payment_method"].str.title().str.strip()
    df["year"] = df["purchase_date"].dt.year
    df["month"] = df["purchase_date"].dt.month
    return df


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    df_clean = preprocess(df)
    df_clean.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned data written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
