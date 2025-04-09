Pix Fraud Detection

O projeto tem como objetivo detectar fraudes em transações via Pix utilizando modelo de machine learning. A solução foi desenvolvida com foco em escalabilidade e interpretabilidade, integrando modelagem, API interativa com Streamlit, e ambiente containerizado com Docker.

Objetivo
Desenvolver um modelo preditivo de classificação binária para identificar possíveis fraudes em transações Pix, utilizando dados com características como scores, valor da transação, horário, regiões do Brasil.

Tecnologias Utilizadas
- Python 3.11
- Streamlit
- Scikit-learn
- XGBoost
- Poetry (gerenciamento de dependências)
- Docker
- Pandas, Joblib e outras.

Estrutura do Projeto

pix-fraud-detection/
├── app/                  # Aplicação Streamlit
├── data/                 # Dados brutos ou processados
├── modelos/              # Modelos treinados (.joblib, .pkl)
├── notebooks/            # Notebooks de EDA e exploração
├── src/                  # Scripts principais do pipeline
│   ├── data_prep.py      # Pré-processamento de dados
│   ├── features.py       # Engenharia de variáveis
│   ├── predict.py        # Lógica de predição
│   └── train.py          # Treinamento do modelo
├── tests/                # Testes unitários e de integração
├── .env                  # Variáveis de ambiente (não versionado)
├── .gitignore
├── Dockerfile            # Docker para deploy da aplicação
├── LICENSE               # Licença do projeto
├── main.py               # Script principal opcional
├── Makefile              # Comandos automáticos
├── poetry.lock           # Lockfile do Poetry
├── pyproject.toml        # Dependências e configurações com Poetry
├── README.md             # Documentação do projeto
├── requirements.txt      # Lista alternativa de dependências (auto-gerado)
├── run_check.py          # Execução de testes da pipeline

Como Executar o Projeto
1. Clonar o repositório
   
git clone https://github.com/JazzGoncalves/pix-fraud-detection.git

cd pix-fraud-detection

3. Rodar com Docker
docker build -t pix-fraud-app .
docker run -p 8501:8501 pix-fraud-app
Acesse http://localhost:8501 no navegador.

4. Rodar localmente (sem Docker)
poetry install
poetry run streamlit run app/app.py
