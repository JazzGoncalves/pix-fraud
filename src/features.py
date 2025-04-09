import pandas as pd
import numpy as np

def create_features(df):
    import numpy as np
    df = df.copy()

    df['fim_de_semana'] = df['dia_semana'].isin([5, 6]).astype(int)
    df['tempo_abertura_anos'] = df['tempo_abertura_conta'] / 365.0
    df['log_valor'] = np.log1p(df['valor'])
    df['score_pld_normalizado'] = df['score_pld'] / 1000.0
    df['valor_acima_1000'] = (df['valor'] > 1000).astype(int)
    df['canal_dispositivo'] = df['canal'] + "_" + df['tipo_dispositivo']
    df['estado_categoria'] = df['estado'] + "_" + df['categoria_cliente']
    df['valor_por_score'] = df['valor'] / (df['score_pld'] + 1)
    df['valor_medio_diario'] = df['valor'] / (df['tempo_abertura_conta'] + 1)

    limite_outlier = df['valor'].quantile(0.99)
    df['valor_muito_alto'] = (df['valor'] > limite_outlier).astype(int)

    df['score_categoria'] = df['categoria_cliente'] + "_" + pd.cut(
        df['score_pld'], bins=[0, 250, 500, 750, 1000],
        labels=["baixa", "média", "alta", "muito_alta"]
    ).astype(str)

    df['manha'] = df['hora'].between(6, 11).astype(int)
    df['madrugada'] = df['hora'].between(0, 5).astype(int)
    df['horario_risco'] = df['manha'] + df['madrugada']

    # Regiões de fronteira
    estados_fronteira = ["RR", "AC", "RO", "AM", "MS", "MT", "AP", "PR"]
    df['estado_fronteira'] = df['estado'].isin(estados_fronteira).astype(int)
    
    df['media_score_estado'] = df.groupby("estado")["score_pld"].transform("mean")

    return df
