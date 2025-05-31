from typing import Literal
from fastapi import APIRouter, Query, Path
from app.services.scraper import get_html_table, parse_processamento_html
from app.services.fallback import (
    get_fallback_processa_viniferas,
    get_fallback_processa_americanas,
    get_fallback_processa_mesa
)
from app.constants import VINIFERAS, AMERICANAS_HIBRIDAS, MESA, SEM_CLASSIFICACAO
from app.models.processamento import ProcessamentoResponse, TipoProcessamentoEnum

router = APIRouter()

TIPOS_PROCESSAMENTO = {
    TipoProcessamentoEnum.VINIFERAS: "subopt_01",
    TipoProcessamentoEnum.AMERICANAS_HIBRIDAS: "subopt_02",
    TipoProcessamentoEnum.MESA: "subopt_03",
    TipoProcessamentoEnum.SEM_CLASSIFICACAO: "subopt_04"
}

FALLBACK_FUNCS = {
    TipoProcessamentoEnum.VINIFERAS: get_fallback_processa_viniferas,
    TipoProcessamentoEnum.AMERICANAS_HIBRIDAS: get_fallback_processa_americanas,
    TipoProcessamentoEnum.MESA: get_fallback_processa_mesa
}

@router.get("/processamento/{ano}", response_model=ProcessamentoResponse,)
def get_processamento(
        ano: int = Path(..., description="Ano para o qual os dados de processamento devem ser retornados", ge=1970, le=2023),
        tipo: TipoProcessamentoEnum = Query(..., description="Categoria de uvas processadas")
    ):
    """
    Retorna os dados de processamento de uvas para o ano e tipo especificado.

    Se não for possível obter os dados online, dados de fallback são utilizados.
    """
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
        raise ValueError("Tipo inválido. Use: " + TipoProcessamentoEnum.VINIFERAS + ", " + TipoProcessamentoEnum.AMERICANAS_HIBRIDAS + ", " + TipoProcessamentoEnum.MESA + " ou " + TipoProcessamentoEnum.SEM_CLASSIFICACAO)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao={subopcao}"