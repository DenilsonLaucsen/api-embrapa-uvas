from fastapi import APIRouter, Query
from app.services.scraper import get_html_table, parse_importacao_html
from app.services.fallback import (
    get_fallback_imp_espumantes,
    get_fallback_imp_passas,
    get_fallback_imp_frescas,
    get_fallback_imp_vinhos,
    get_fallback_imp_suco
)
from app.constants import VINHOS_DE_MESA, ESPUMANTES, UVAS_FRESCAS, UVAS_PASSAS, SUCO_DE_UVA

router = APIRouter()

TIPOS_IMPORTACAO = {
    VINHOS_DE_MESA: "subopt_01",
    ESPUMANTES: "subopt_02",
    UVAS_FRESCAS: "subopt_03",
    UVAS_PASSAS: "subopt_04",
    SUCO_DE_UVA: "subopt_05"
}

FALLBACK_FUNCS = {
    VINHOS_DE_MESA: get_fallback_imp_vinhos,
    ESPUMANTES: get_fallback_imp_espumantes,
    UVAS_FRESCAS: get_fallback_imp_frescas,
    UVAS_PASSAS: get_fallback_imp_passas,
    SUCO_DE_UVA: get_fallback_imp_suco,
}

@router.get("/importacao/{ano}")
def get_importacao(ano: int, tipo: str = Query(..., description=VINHOS_DE_MESA + " | " + ESPUMANTES + " | " + UVAS_FRESCAS + " | " + UVAS_PASSAS + " | " + SUCO_DE_UVA)):
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
        raise ValueError("Tipo inválido. Use: " + VINHOS_DE_MESA + ", " + ESPUMANTES + ", " + UVAS_FRESCAS + ", " + UVAS_PASSAS + " ou " + SUCO_DE_UVA)
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao={subopcao}"