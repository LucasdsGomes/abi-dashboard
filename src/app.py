import streamlit as st
import pandas as pd
import json
from loader import load_data
from kpis import calculate_kpis
from comparison import compare_last_two_months
from score import business_score
from insights import generate_insights
from metrics import dataset_overview
from report_pdf import generate_pdf_report


st.set_page_config(
    page_title="Business Analytics Dashboard",
    layout="wide"
)

st.title("📊 Business Analytics Dashboard")
st.caption("Análise de performance, saúde do negócio e insights automáticos")

uploaded_file = st.file_uploader(
    "📁 Faça upload do arquivo CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["date"] = pd.to_datetime(df["date"])

    if "revenue" not in df.columns:
        df["revenue"] = df["quantity"] * df["price"]

    st.subheader("🔍 Pré-visualização dos dados")
    st.dataframe(df.head())

    st.subheader("📌 Visão Geral do Dataset")

    overview = dataset_overview(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Linhas", overview["Número de linhas"])
    col2.metric("Colunas", overview["Número de colunas"])
    col3.metric(
        "Dados faltantes (%)",
        f"{overview['Percentual de valores faltantes']:.2f}%"
    )

    st.markdown("### 🧩 Estrutura das Colunas")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📊 Colunas Numéricas**")
        st.write(list(overview["Colunas Numéricas"]))

    with col2:
        st.markdown("**🔤 Colunas Categóricas**")
        st.write(list(overview["Colunas Categóricas"]))

    st.markdown("### ⚠️ Valores nulos por coluna")

    nulls_df = (
        pd.DataFrame
        .from_dict(overview["Valores nulos por coluna"], orient="index")
        .reset_index()
        .rename(columns={"index": "Coluna", 0: "Valores nulos"})
    )

    st.dataframe(nulls_df)

    st.subheader("📈 KPIs Principais")
    kpis = calculate_kpis(df)

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    kpi1.metric("💰 Receita Total", f"R$ {kpis['total_revenue']:.2f}")
    kpi2.metric("🏷️ Preço Médio", f"R$ {kpis['average_price']:.2f}")
    kpi3.metric("📦 Produto Top", kpis["top_product"])
    kpi4.metric("👤 Cliente Top", kpis["top_customer"])
    kpi5.metric("🔢 Quantidade Total", kpis["total_quantity"])

    st.subheader("📆 Comparação de Períodos")
    revenue_trend = compare_last_two_months(df)

    if revenue_trend.get("status"):
        st.warning(revenue_trend["status"])
    else:
        st.metric(
            label=f"Variação ({revenue_trend['previous_period']} → {revenue_trend['current_period']})",
            value=f"R$ {revenue_trend['current_revenue']:.2f}",
            delta=f"{revenue_trend['variation_percent']}%"
        )

    st.subheader("🚦 Business Score")
    business = business_score(df)
    score = business["score"]

    if score >= 85:
        st.success(f"🟢 Negócio saudável — Score: {score}")
    elif score >= 65:
        st.warning(f"🟡 Atenção necessária — Score: {score}")
    else:
        st.error(f"🔴 Risco elevado — Score: {score}")


    st.subheader("🧠 Insights Automáticos")
    insights = []

    #

    if revenue_trend.get("variation_percent", 0) < 0:
        insights.append("Receita apresentou queda no último período.")

    if score < 65:
        insights.append("Score geral indica risco operacional.")

    if not insights:
        st.success("Nenhum risco relevante identificado 🎉")
    else:
        for insight in insights:
            st.warning(f"• {insight}")

    st.subheader("📤 Exportar Relatório Executivo")

    final_report = generate_insights(
        df=df,
        revenue_trend=revenue_trend,
        business_score=business
    )

    report_json = json.dumps(final_report, indent=4, ensure_ascii=False)

    st.download_button(
        label="📄 Baixar relatório executivo (JSON)",
        data=report_json,
        file_name="executive_report.json",
        mime="application/json"
    )

    st.subheader("📄 Exportar Relatório em PDF")

    if st.button("Gerar PDF"):
        pdf_path = "relatorio_executivo.pdf"

        generate_pdf_report(
            file_path=pdf_path,
            overview=dataset_overview(df),
            kpis=kpis,
            revenue_trend=revenue_trend,
            business_score=business,
            insights=insights
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Baixar relatório em PDF",
                data=f,
                file_name="relatorio_executivo.pdf",
                mime="application/pdf"
            )


else:
    st.info("⬆️ Envie um arquivo CSV para iniciar a análise.")
