import pandas as pd

def dataset_overview(df):
    """Retorna uma visão geral do dataset."""
    overview = {
        "Número de linhas": df.shape[0],
        "Número de colunas": df.shape[1],
        "Colunas": df.columns.tolist(),
        "Tipos de dados": df.dtypes.astype(str).to_dict(),
        "Colunas Numéricas": df.select_dtypes(include="number").columns.tolist(),
        "Colunas Categóricas": df.select_dtypes(exclude="number").columns.tolist(),
        "Valores nulos por coluna": df.isnull().sum().to_dict(),
        "Estatísticas descritivas": df.describe().to_dict(),
        "Percentual de valores faltantes": (
            df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100
        ) if df.shape[0] > 0 else 0,
    }
    return overview
