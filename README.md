# Analytics Engineering: Pipeline de Desembolsos do BNDES

Este projeto apresenta uma solução completa de engenharia e modelagem de dados utilizando os conceitos da **Modern Data Stack**. O objetivo do pipeline é extrair dados brutos de desembolsos através da API pública do BNDES (plataforma CKAN), orquestrar o armazenamento em um Data Lake na nuvem, transformar os dados via dbt no BigQuery e disponibilizar os insights em um dashboard.

---

## 🏗️ Arquitetura de Dados

`API ` ➡️ `Python (Docker)` ➡️ `Google Cloud Storage (Bronze)` ➡️ `BigQuery (Silver)` ➡️ `dbt Core (Gold)` ➡️ `Looker Studio (Em construção)`

1. **Ingestão:** Script Python conteinerizado em Docker extrai os dados brutos e salva em formato colunar Parquet.
2. **Data Lake:** Armazenamento estruturado no Google Cloud Storage (GCS).
3. **Data Warehouse:** Mapeamento via External Tables no BigQuery para redução de custos.
4. **Transformação (dbt):** Modelagem lógica separada em camadas Staging (Silver) e Marts (Gold).

---
*Nota: Repositório em fase final de documentação. Próxima etapa: Conexão e publicação do Dashboard no Looker Studio.*
