import pandas as pd
import requests
from google.cloud import storage
import io

def extrair_e_carregar_bndes():
    # 1. Configurações da API do BNDES (CKAN)
    url_api = "https://dadosabertos.bndes.gov.br/api/3/action/datastore_search"
    parametros = {
        "resource_id": "179950b8-b504-4cc7-b0db-9c9eed99e9ba",
        "limit": 100 
    }
    
    # 2. Configurações da GCP (Altere para o nome do seu bucket!)
    NOME_BUCKET = "landing-zone-bndes-manuel"
    NOME_ARQUIVO_ALVO = "raw/desembolsos_bndes/ano_mes=2026/dados_brutos.parquet"

    print("[INGESTÃO] 🚀 Iniciando requisição para a API do BNDES...")
    
    try:
        # Requisição para a API
        response = requests.get(url_api, params=parametros, timeout=30)
        
        if response.status_code == 200:
            resposta_json = response.json()
            
            if resposta_json.get("success"):
                registros = resposta_json["result"]["records"]
                df = pd.DataFrame(registros)
                print(f"✅ [SUCESSO] Dados extraídos da API. Linhas capturadas: {len(df)}")
                
                # --- INÍCIO DA CARGA PARA O DATA LAKE ---
                print(f"[CLOUD] ☁️ Conectando ao Google Cloud Storage...")
                
                # Inicializa o cliente do Storage (ele lê a variável de ambiente automaticamente)
                storage_client = storage.Client()
                bucket = storage_client.bucket(NOME_BUCKET)
                blob = bucket.blob(NOME_ARQUIVO_ALVO)
                
                # Convertendo o DataFrame para o formato Parquet na memória (sem salvar no disco do container)
                buffer = io.BytesIO()
                df.to_parquet(buffer, index=False)
                buffer.seek(0)
                
                print(f"[CLOUD] 📤 Enviando arquivo para o bucket {NOME_BUCKET}...")
                # Faz o upload do arquivo
                blob.upload_from_file(buffer, content_type="application/octet-stream")
                
                print(f"🎉 [SUCESSO ABSOLUTO] Dados brutos salvos com sucesso no Data Lake!")
                print(f"📍 Caminho: gs://{NOME_BUCKET}/{NOME_ARQUIVO_ALVO}")
                
            else:
                print("⚠️ A API respondeu, mas o CKAN retornou sucesso = False.")
        else:
            print(f"❌ [ERRO] Falha na API. Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"💥 [FALHA] Erro crítico no pipeline: {str(e)}")

if __name__ == "__main__":
    extrair_e_carregar_bndes()