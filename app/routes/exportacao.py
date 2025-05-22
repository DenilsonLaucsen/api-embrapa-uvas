from fastapi import APIRouter, Query
from app.services.scraper import get_html_table

router = APIRouter()

TIPOS_EXPORTACAO = {
    "vinhos_de_mesa": "subopt_01",
    "espumantes": "subopt_02",
    "uvas_frescas": "subopt_03",
    "suco_de_uva": "subopt_04"
}

@router.get("/exportacao/{ano}")
def get_exportacao(ano: int, tipo: str = Query(..., description="vinhos_de_mesa | espumantes | uvas_frescas | suco_de_uva")):
    try:
        url = url_exportacao(ano, tipo)
        dados = get_html_table(url)
        return {"ano": ano, "tipo": tipo, "dados": dados}
    except Exception as e:
        return {"erro": str(e)}

def url_exportacao(ano: int, tipo: str) -> str:
    subopcao = TIPOS_EXPORTACAO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: vinhos_de_mesa, espumantes, uvas_frescas ou suco_de_uva.")
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao={subopcao}"