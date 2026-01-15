def generate_insights(df, revenue_trend: dict, business_score: dict) -> list[str]:
    insights = []

    # 📉 Receita
    if revenue_trend.get("trend") == "down":
        insights.append(
            f"⚠️ A receita caiu {abs(revenue_trend['variation_percent'])}% em relação ao período anterior."
        )
    elif revenue_trend.get("trend") == "up":
        insights.append(
            f"📈 A receita cresceu {revenue_trend['variation_percent']}% no último período."
        )

    # 📦 Concentração de produto
    if not df.empty:
        top_product_revenue = df.groupby("product")["revenue"].sum().max()
        total_revenue = df["revenue"].sum()

        if total_revenue > 0:
            concentration_ratio = top_product_revenue / total_revenue

            if concentration_ratio > 0.5:
                insights.append(
                    "📦 Alta concentração de receita em um único produto pode representar risco ao negócio."
                )

    # 👥 Diversidade de clientes
    unique_customers = df["customer"].nunique()
    if unique_customers < 5:
        insights.append(
            "👥 Baixa diversidade de clientes detectada. O negócio pode estar dependente de poucos compradores."
        )

    # 🏁 Score final
    score = business_score["score"]
    if score >= 85:
        insights.append("✅ Excelente saúde do negócio.")
    elif score >= 65:
        insights.append("⚠️ Saúde moderada do negócio. Há pontos de atenção.")
    else:
        insights.append("🚨 Saúde crítica do negócio. Ações corretivas são recomendadas.")

    return insights
