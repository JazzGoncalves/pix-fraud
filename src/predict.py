import joblib
import numpy as np
import pandas as pd

def carregar_modelo(model_path: str):
    return joblib.load(model_path)

def fazer_predicao(df: pd.DataFrame, modelo) -> pd.DataFrame:
    df_resultado = df.copy()
    proba = modelo.predict_proba(df_resultado)[:, 1]
    df_resultado["score_fraude"] = np.round(proba * 10) / 10
    return df_resultado



