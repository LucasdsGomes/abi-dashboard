from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def generate_pdf_report(
    file_path: str,
    overview: dict,
    kpis: dict,
    revenue_trend: dict,
    business_score: dict,
    insights: list
):
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("<b>Relatório Executivo de Análise de Dados</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Visão Geral
    elements.append(Paragraph("<b>Visão Geral do Dataset</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Linhas: {overview['Número de linhas']}", styles["Normal"]))
    elements.append(Paragraph(f"Colunas: {overview['Número de colunas']}", styles["Normal"]))
    elements.append(
        Paragraph(
            f"Percentual de dados faltantes: {overview['Percentual de valores faltantes']:.2f}%",
            styles["Normal"]
        )
    )
    elements.append(Spacer(1, 12))

    # KPIs
    elements.append(Paragraph("<b>KPIs Principais</b>", styles["Heading2"]))
    for k, v in kpis.items():
        elements.append(Paragraph(f"{k.replace('_', ' ').title()}: {v}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Comparação de períodos
    elements.append(Paragraph("<b>Comparação de Receita</b>", styles["Heading2"]))
    if "status" in revenue_trend:
        elements.append(Paragraph(revenue_trend["status"], styles["Normal"]))
    else:
        elements.append(
            Paragraph(
                f"{revenue_trend['previous_period']} → {revenue_trend['current_period']}<br/>"
                f"Variação: {revenue_trend['variation_percent']}%",
                styles["Normal"]
            )
        )
    elements.append(Spacer(1, 12))

    # Score
    elements.append(Paragraph("<b>Business Score</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Score final: {business_score['score']}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Insights
    elements.append(Paragraph("<b>Insights</b>", styles["Heading2"]))
    for insight in insights:
        elements.append(Paragraph(f"- {insight}", styles["Normal"]))

    doc.build(elements)
