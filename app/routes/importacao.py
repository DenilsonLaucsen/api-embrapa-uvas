from typing import Literal
from fastapi import APIRouter, Query, Path
from app.services.scraper import get_html_table, parse_importacao_html
from app.services.fallback import (
    get_fallback_imp_espumantes,
    get_fallback_imp_passas,
    get_fallback_imp_frescas,
    get_fallback_imp_vinhos,
    get_fallback_imp_suco
)
from app.constants import VINHOS_DE_MESA, ESPUMANTES, UVAS_FRESCAS, UVAS_PASSAS, SUCO_DE_UVA
from app.models.importacao import ImportacaoResponse, TipoImportacaoEnum

router = APIRouter()

TIPOS_IMPORTACAO = {
    TipoImportacaoEnum.VINHOS_DE_MESA: "subopt_01",
    TipoImportacaoEnum.ESPUMANTES: "subopt_02",
    TipoImportacaoEnum.UVAS_FRESCAS: "subopt_03",
    TipoImportacaoEnum.UVAS_PASSAS: "subopt_04",
    TipoImportacaoEnum.SUCO_DE_UVA: "subopt_05"
}

FALLBACK_FUNCS = {
    TipoImportacaoEnum.VINHOS_DE_MESA: get_fallback_imp_vinhos,
    TipoImportacaoEnum.ESPUMANTES: get_fallback_imp_espumantes,
    TipoImportacaoEnum.UVAS_FRESCAS: get_fallback_imp_frescas,
    TipoImportacaoEnum.UVAS_PASSAS: get_fallback_imp_passas,
    TipoImportacaoEnum.SUCO_DE_UVA: get_fallback_imp_suco,
}

@router.get("/importacao/{ano}", response_model=ImportacaoResponse)
def get_importacao(
        ano: int = Path(..., description="Ano para o qual os dados de importação devem ser retornados", ge=1970, le=2024),
        tipo: TipoImportacaoEnum = Query(..., description="Categoria de uvas importadas")
    ):
    """
    Retorna os dados de importação de uvas para o ano e tipo especificado.

    Se não for possível obter os dados online, dados de fallback são utilizados.
    """
    url = url_importacao(ano, tipo)
    try:
        tabela = get_html_table(url)
        dados = parse_importacao_html(tabela, ano)
        return {"tipo": tipo, "dados": dados, "fonte": "scraper"}
    except Exception as e:
        dados = FALLBACK_FUNCS.get(tipo.lower(), lambda x: [{"erro": "tipo inválido para fallback"}])(ano)
        return {"tipo": tipo, "dados": dados, "fonte": "fallback"}
    
def url_importacao(ano: int, tipo: str) -> str:
    subopcao = TIPOS_IMPORTACAO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: " + TipoImportacaoEnum.VINHOS_DE_MESA + ", " + TipoImportacaoEnum.ESPUMANTES + ", " + TipoImportacaoEnum.UVAS_FRESCAS + ", " + TipoImportacaoEnum.UVAS_PASSAS + " ou " + TipoImportacaoEnum.SUCO_DE_UVA)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao={subopcao}"