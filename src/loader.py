import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    # Validação mínima
    required_columns = {"date", "quantity", "price"}
    missing_cols = required_columns - set(df.columns)

    if missing_cols:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing_cols}")

    # Conversão de data
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Criação da receita
    if "revenue" not in df.columns:
        df["revenue"] = df["quantity"] * df["price"]

    return df
