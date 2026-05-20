with fonte_dados as (
    select * from {{ source('ckan_bndes', 'ext_desembolsos') }}
)

select
    safe_cast(ano as int64) as ano_desembolso,
    safe_cast(mes as int64) as mes_desembolso,
    trim(setor_bndes) as nome_setor,
    trim(subsetor_bndes) as nome_subsetor,
    safe_cast(desembolsos_reais as float64) as valor_desembolsado_reais
from fonte_dados
