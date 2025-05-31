from typing import Literal
from fastapi import APIRouter, Query, Path
from app.services.scraper import get_html_table, parse_exportacao_html
from app.services.fallback import (
    get_fallback_exp_espumantes,
    get_fallback_exp_vinhos,
    get_fallback_exp_suco,
    get_fallback_exp_uva
)
from app.constants import VINHOS_DE_MESA, ESPUMANTES, UVAS_FRESCAS, SUCO_DE_UVA
from app.models.exportacao import ExportacaoResponse, TipoExportacaoEnum

router = APIRouter()

TIPOS_EXPORTACAO = {
    TipoExportacaoEnum.VINHOS_DE_MESA: "subopt_01",
    TipoExportacaoEnum.ESPUMANTES: "subopt_02",
    TipoExportacaoEnum.UVAS_FRESCAS: "subopt_03",
    TipoExportacaoEnum.SUCO_DE_UVA: "subopt_04"
}

FALLBACK_FUNCS = {
    TipoExportacaoEnum.VINHOS_DE_MESA: get_fallback_exp_vinhos,
    TipoExportacaoEnum.ESPUMANTES: get_fallback_exp_espumantes,
    TipoExportacaoEnum.UVAS_FRESCAS: get_fallback_exp_uva,
    TipoExportacaoEnum.SUCO_DE_UVA: get_fallback_exp_suco,
}

@router.get("/exportacao/{ano}", response_model=ExportacaoResponse)
def get_exportacao(
        ano: int = Path(..., description="Ano para o qual os dados de exportação devem ser retornados", ge=1970, le=2024),
        tipo: TipoExportacaoEnum = Query(..., description="Categoria de uvas exportadas")
    ):
    """
    Retorna os dados de exportação de uvas para o ano e tipo especificado.

    Se não for possível obter os dados online, dados de fallback são utilizados.
    """
    url = url_exportacao(ano, tipo)
    try:
        tabela = get_html_table(url)
        dados = parse_exportacao_html(tabela, ano)
        return {"tipo": tipo, "dados": dados, "fonte": "scraper"}
    except Exception as e:
        dados = FALLBACK_FUNCS.get(tipo.lower(), lambda x: [{"erro": "tipo inválido para fallback"}])(ano)
        return {"tipo": tipo, "dados": dados, "fonte": "fallback"}

def url_exportacao(ano: int, tipo: str) -> str:
    subopcao = TIPOS_EXPORTACAO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: " + TipoExportacaoEnum.VINHOS_DE_MESA + ", " + TipoExportacaoEnum.ESPUMANTES + ", " + TipoExportacaoEnum.UVAS_FRESCAS + "ou " + TipoExportacaoEnum.SUCO_DE_UVA)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao={subopcao}"