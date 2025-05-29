from fastapi import APIRouter, Query
from app.services.scraper import get_html_table, parse_exportacao_html
from app.services.fallback import (
    get_fallback_exp_espumantes,
    get_fallback_exp_vinhos,
    get_fallback_exp_suco,
    get_fallback_exp_uva
)
from app.constants import VINHOS_DE_MESA, ESPUMANTES, UVAS_FRESCAS, SUCO_DE_UVA

router = APIRouter()

TIPOS_EXPORTACAO = {
    VINHOS_DE_MESA: "subopt_01",
    ESPUMANTES: "subopt_02",
    UVAS_FRESCAS: "subopt_03",
    SUCO_DE_UVA: "subopt_04"
}

FALLBACK_FUNCS = {
    VINHOS_DE_MESA: get_fallback_exp_vinhos,
    ESPUMANTES: get_fallback_exp_espumantes,
    SUCO_DE_UVA: get_fallback_exp_suco,
    UVAS_FRESCAS: get_fallback_exp_uva,
}

@router.get("/exportacao/{ano}")
def get_exportacao(ano: int, tipo: str = Query(..., description=VINHOS_DE_MESA + " | " + ESPUMANTES + " | " + UVAS_FRESCAS + " | " + SUCO_DE_UVA)):
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
        raise ValueError("Tipo inválido. Use: " + VINHOS_DE_MESA + ", " + ESPUMANTES + ", " + UVAS_FRESCAS + "ou " + SUCO_DE_UVA)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao={subopcao}"