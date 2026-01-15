import pandas as pd

def compare_last_two_months(df: pd.DataFrame) -> dict:
    df = df.copy()
    df["year_month"] = df["date"].dt.to_period("M")

    grouped = (
        df.groupby("year_month")["revenue"]
        .sum()
        .sort_index()
    )

    if len(grouped) < 2:
        return {
            "status": "insufficient_data"
        }

    current_period = grouped.index[-1]
    previous_period = grouped.index[-2]

    current_revenue = grouped.loc[current_period]
    previous_revenue = grouped.loc[previous_period]

    variation = (
        (current_revenue - previous_revenue) / previous_revenue * 100
        if previous_revenue != 0 else 0
    )

    trend = (
        "up" if variation > 0
        else "down" if variation < 0
        else "stable"
    )

    return {
        "current_period": str(current_period),
        "previous_period": str(previous_period),
        "current_revenue": round(float(current_revenue), 2),
        "previous_revenue": round(float(previous_revenue), 2),
        "variation_percent": round(float(variation), 2),
        "trend": trend
    }
