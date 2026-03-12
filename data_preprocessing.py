"""Data preprocessing for the customer shopping behavior dataset."""

import pathlib
import pandas as pd

DATA_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "customer_shopping_behavior.csv"
OUTPUT_PATH = pathlib.Path(__file__).resolve().parents[1] / "data" / "customer_shopping_behavior_cleaned.csv"


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic cleaning and feature engineering."""

    df = df.copy()
    # Convert date
    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")

    # Standardize text fields
    df["gender"] = df["gender"].str.upper().str.strip()
    df["payment_method"] = df["payment_method"].str.title().str.strip()

    # Derive additional columns
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
