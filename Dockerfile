FROM python:3.11-slim

WORKDIR /app

# Comando obrigatório para instalar o git no linux slim
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credenciais-gcp.json

CMD ["dbt", "debug", "--project-dir", "/app/dbt_bndes", "--profiles-dir", "/root/.dbt"]

