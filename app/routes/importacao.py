from fastapi import APIRouter, Query
from app.services.scraper import get_html_table

router = APIRouter()

TIPOS_IMPORTACAO = {
    "vinhos_de_mesa": "subopt_01",
    "espumantes": "subopt_02",
    "uvas_frescas": "subopt_03",
    "uvas_passas": "subopt_04",
    "suco_de_uva": "subopt_05"
}

@router.get("/importacao/{ano}")
def get_importacao(ano: int, tipo: str = Query(..., description="vinhos_de_mesa | espumantes | uvas_frescas | uvas_passas | suco_de_uva")):
    try:
        url = url_importacao(ano, tipo)
        dados = get_html_table(url)
        return {"ano": ano, "tipo": tipo, "dados": dados}
    except Exception as e:
        return {"erro": str(e)}
    
def url_importacao(ano: int, tipo: str) -> str:
    subopcao = TIPOS_IMPORTACAO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: vinhos_de_mesa, espumantes, uvas_frescas, uvas_passas ou suco_de_uva.")
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao={subopcao}"