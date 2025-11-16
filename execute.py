import pandas as pd

def main():
    df = pd.read_csv("data.csv")

    # Fix the column name issue (the original file had "revenew" typo)
    if "revenew" in df.columns:
        df = df.rename(columns={"revenew": "revenue"})

    # Compute summary
    result = {
        "total_rows": len(df),
        "total_revenue": float(df["revenue"].sum()),
        "max_revenue": float(df["revenue"].max()),
        "min_revenue": float(df["revenue"].min()),
    }

    print(pd.Series(result).to_json())

if __name__ == "__main__":
    main()

