import pytest
import pandas as pd
from src.features import create_features
from src.predict import carregar_modelo, fazer_predicao

def test_fazer_predicao():
    df = pd.DataFrame({
        "valor": [500],
        "dia_semana": [3],
        "tempo_abertura_conta": [200],
        "score_pld": [600],
        "canal": ["web"],
        "tipo_dispositivo": ["desktop"],
        "estado": ["RJ"],
        "categoria_cliente": ["pequeno_empresario"],
        "status_src": ["regular"],
        "data_hora": ["2024-01-01 10:00:00"],
        "regiao": ["Sudeste"]
    })
    df["data_hora"] = pd.to_datetime(df["data_hora"])
    df["hora"] = df["data_hora"].dt.hour

    df_feat = create_features(df)

    modelo = carregar_modelo("modelos/modelo_fraude_pix.pkl")
    df_pred = fazer_predicao(df_feat, modelo)

    assert "score_fraude" in df_pred.columns
    assert df_pred["score_fraude"].between(0, 10).all()
