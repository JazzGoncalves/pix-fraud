import numpy as np
import pandas as pd

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["fim_de_semana"] = df["dia_semana"].isin([5, 6]).astype(int)
    df["tempo_abertura_anos"] = df["tempo_abertura_conta"] / 365
    df["log_valor"] = np.log1p(df["valor"])
    df["score_pld_normalizado"] = df["score_pld"] / 1000
    df["valor_acima_1000"] = (df["valor"] > 1000).astype(int)
    df["canal_dispositivo"] = df["canal"] + "_" + df["tipo_dispositivo"]
    df["estado_categoria"] = df["estado"] + "_" + df["categoria_cliente"]
    return df
  
def carregar_dados(caminho: str) -> pd.DataFrame:
    df = pd.read_parquet(caminho)
    df['data_hora'] = pd.to_datetime(df['data_hora'])
    df['hora'] = df['data_hora'].dt.hour
    df['dia_semana'] = df['data_hora'].dt.dayofweek
    return df