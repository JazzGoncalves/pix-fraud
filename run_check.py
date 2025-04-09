import pandas as pd
from src.features import create_features
from src.train import train_model
from src.predict import carregar_modelo, fazer_predicao

def main():
    print("\nIniciando validação do pipeline...\n")

    caminho_dados = "data/dados_pix_2024.parquet"
    caminho_modelo = "modelos/modelo_fraude_pix.pkl"

    # 1. Dados
    df = pd.read_parquet(caminho_dados)
    df['data_hora'] = pd.to_datetime(df['data_hora'])
    df['hora'] = df['data_hora'].dt.hour
    df['dia_semana'] = df['data_hora'].dt.dayofweek

    # 2. Features
    df_feat = create_features(df)

    # 3. Treino
    train_model(df_feat, path_model=caminho_modelo)

    # 4. Modelo salvo
    modelo = carregar_modelo(caminho_modelo)

    # 5. Predições
    df_pred = fazer_predicao(df_feat, modelo)

    # 6. Resultados
    print("\nTop 10 transações com maiores scores de fraude:")
    print(df_pred[["id_transacao", "valor", "score_fraude"]].sort_values(by="score_fraude", ascending=False).head(10))

if __name__ == "__main__":
    main()
