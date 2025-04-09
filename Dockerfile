# Imagem base
FROM python:3.11-slim

# Variável de ambiente
ENV POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1

# Dependências
RUN apt-get update && apt-get install -y \
    build-essential curl git && \
    rm -rf /var/lib/apt/lists/*

# Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Diretório de trabalho
WORKDIR /app

# Arquivos do projeto
COPY . .

# Dependências com poetry
RUN poetry install --no-root --only main --no-interaction

# Streamlit
EXPOSE 8501

# Comando para iniciar o app
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
