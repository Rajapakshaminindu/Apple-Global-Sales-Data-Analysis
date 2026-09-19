"""
Apple Global Sales - Exploratory Data Analysis (EDA) Module
Converts exploratory notebook workflows into reusable functions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_sales_data(filepath: str) -> pd.DataFrame:
    """Load Apple sales dataset and inspect basic metrics."""
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df


def summarize_missing_values(df: pd.DataFrame) -> pd.Series:
    """Check for missing or null values across features."""
    missing = df.isnull().sum()
    print("Missing values summary:\n", missing[missing > 0])
    return missing


def plot_price_vs_discount(df: pd.DataFrame, output_path: str = "price_vs_discount.png"):
    """Visualize correlation between unit price and discounted price."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="unit_price_usd", y="discounted_price_usd", hue="region", data=df, alpha=0.8)
    plt.title("Unit Price vs Discounted Price by Region (USD)")
    plt.xlabel("Unit Price ($)")
    plt.ylabel("Discounted Price ($)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Saved plot to {output_path}")


def compute_regional_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales revenue by region."""
    if "revenue_local_currency" in df.columns and "region" in df.columns:
        summary = df.groupby("region")["revenue_local_currency"].agg(["count", "sum", "mean"]).reset_index()
        summary.rename(columns={"count": "total_transactions", "sum": "total_revenue", "mean": "avg_order_value"}, inplace=True)
        return summary
    return pd.DataFrame()


if __name__ == "__main__":
    DATA_PATH = "apple_global_sales_dataset.csv"
    try:
        sales_df = load_sales_data(DATA_PATH)
        summarize_missing_values(sales_df)
        plot_price_vs_discount(sales_df)
        revenue_summary = compute_regional_revenue(sales_df)
        print("\n--- Regional Revenue Breakdown ---")
        print(revenue_summary)
    except FileNotFoundError:
        print(f"Dataset '{DATA_PATH}' not found. Please ensure it is present in the working directory.")
