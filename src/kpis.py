def calculate_kpis(df) -> dict:
    total_revenue = df["revenue"].sum()
    average_price = df["price"].mean()
    top_product = df["product"].value_counts().idxmax()
    top_customer = df["customer"].value_counts().idxmax()
    total_quantity = df["quantity"].sum()

    return {
        "total_revenue": round(total_revenue, 2),
        "average_price": round(average_price, 2),
        "top_product": top_product,
        "top_customer": top_customer,
        "total_quantity": int(total_quantity),
    }
