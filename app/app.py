import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from src.predict import carregar_modelo, fazer_predicao
from src.features import create_features

st.set_page_config(page_title="Fraude Pix Detector", layout="wide")
st.title("Detecção de Fraudes via Pix")

uploaded_file = st.file_uploader("Envie um arquivo `.csv` para predição de score de fraude:", type=["csv"])

if uploaded_file:
    with st.spinner("Lendo o arquivo..."):
        df = pd.read_csv(uploaded_file)
        st.subheader("Pré-visualização dos dados originais")
        st.dataframe(df.head())

        # Transformações
        df['data_hora'] = pd.to_datetime(df['data_hora'])
        df['hora'] = df['data_hora'].dt.hour
        df['dia_semana'] = df['data_hora'].dt.dayofweek

        st.info("✨ Criando novas features...")
        df_feat = create_features(df)

        modelo = carregar_modelo("modelos/modelo_fraude_pix.pkl")

        st.info("Gerando os scores de fraude...")
        df_resultado = fazer_predicao(df_feat, modelo)

        st.success("Predições realizadas com sucesso!")

        st.subheader("Transações com maiores scores de fraude")
        st.dataframe(
            df_resultado.sort_values(by="score_fraude", ascending=False)[["id_transacao", "valor", "score_fraude"]].reset_index(drop=True)
        )
        csv = df_resultado.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Baixar resultados com score",
            data=csv,
            file_name="predicoes_pix.csv",
            mime="text/csv"
        )
else:
    st.warning("Faça o upload de um arquivo para começar.")
