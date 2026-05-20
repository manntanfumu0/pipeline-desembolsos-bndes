with dados_silver as (
    select * from {{ ref('stg_desembolsos') }}
)

select
    ano_desembolso,
    nome_setor,
    count(*) as quantidade_operacoes,
    round(sum(valor_desembolsado_reais), 2) as total_desembolsado_reais,
    round(avg(valor_desembolsado_reais), 2) as media_desembolsada_reais
from dados_silver
group by 1, 2
order by ano_desembolso desc, total_desembolsado_reais desc
