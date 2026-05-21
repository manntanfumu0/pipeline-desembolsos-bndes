FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema se necessário (o git pode ser ignorado na ingestão pura)
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos locais (incluindo extract_bndes.py e credentials.json)
COPY . .

# Variável que aponta para o JSON de credenciais que você baixou da GCP
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json

# Força o container a executar estritamente o script da ingestão
CMD ["python", "extract_bndes.py"]

