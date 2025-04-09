import os
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier

def train_model(df: pd.DataFrame, target_col: str = "fraude", path_model="modelos/modelo_fraude_pix.pkl", path_features="modelos/features_utilizadas.pkl"):
    df = df.copy()
    y = df[target_col].astype(int)

    colunas_remover = ["id_transacao", "id_remetente", "id_destinatario", "data_hora"]
    df = df.drop(columns=colunas_remover + [target_col], errors="ignore")

    # Separação dados numéricos e categóricos
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols)
    ], remainder='passthrough')

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("xgb", XGBClassifier(
            objective="binary:logistic",
            eval_metric="auc",
            use_label_encoder=False,
            max_depth=5,
            n_estimators=300,
            learning_rate=0.05,
            scale_pos_weight=(y == 0).sum() / (y == 1).sum(),
            random_state=42
        ))
    ])
    model.fit(df, y)
    os.makedirs("modelos", exist_ok=True)
    joblib.dump(model, path_model)
    print("Modelo treinado e pipeline salvo com sucesso.")
