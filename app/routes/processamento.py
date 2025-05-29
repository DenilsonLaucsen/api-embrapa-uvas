from fastapi import APIRouter, Query
from app.services.scraper import get_html_table, parse_processamento_html
from app.services.fallback import (
    get_fallback_processa_viniferas,
    get_fallback_processa_americanas,
    get_fallback_processa_mesa
)
from app.constants import VINIFERAS, AMERICANAS_HIBRIDAS, MESA, SEM_CLASSIFICACAO

router = APIRouter()

TIPOS_PROCESSAMENTO = {
    VINIFERAS: "subopt_01",
    AMERICANAS_HIBRIDAS: "subopt_02",
    MESA: "subopt_03",
    SEM_CLASSIFICACAO: "subopt_04"
}

FALLBACK_FUNCS = {
    VINIFERAS: get_fallback_processa_viniferas,
    AMERICANAS_HIBRIDAS: get_fallback_processa_americanas,
    MESA: get_fallback_processa_mesa
}

@router.get("/processamento/{ano}")
def get_processamento(ano: int, tipo: str = Query(..., description=VINIFERAS + " | " + AMERICANAS_HIBRIDAS + " | " + MESA + " | " + SEM_CLASSIFICACAO)):
    url = url_processamento(ano, tipo)
    try:
        tabela = get_html_table(url)
        dados = parse_processamento_html(tabela, ano)
        return {"tipo": tipo, "dados": dados, "fonte": "scraper"}
    except Exception as e:
        dados = FALLBACK_FUNCS.get(tipo.lower(), lambda x: [{"erro": "tipo inválido para fallback"}])(ano)
        return {"tipo": tipo, "dados": dados, "fonte": "fallback"}

def url_processamento(ano: int, tipo: str) -> str:
    subopcao = TIPOS_PROCESSAMENTO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: " + VINIFERAS + ", " + AMERICANAS_HIBRIDAS + ", " + MESA + " ou " + SEM_CLASSIFICACAO)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao={subopcao}"