from comparison import compare_last_two_months

def business_score(df) -> dict:
    score = 100

    # Queda de Receita -> -20
    revenue_trend = compare_last_two_months(df)
    if revenue_trend.get("trend") == "down":
        score -= 20

    # Alta Concentração de Receita -> -15
    if not df.empty:
        top_product_revenue = df.groupby("product")["revenue"].sum().max()
        total_revenue = df["revenue"].sum()
        concentration_ratio = (
            top_product_revenue / total_revenue if total_revenue > 0 else 0
        )

        if concentration_ratio > 0.5:
            score -= 15

    # Baixa Diversidade de Clientes -> -10
    unique_customers = df["customer"].nunique()
    if unique_customers < 5:
        score -= 10

    return {
        "score": max(score, 0)
    }
