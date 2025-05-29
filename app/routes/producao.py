from fastapi import APIRouter
from app.services.scraper import get_html_table, parse_producao_html
from app.services.fallback import get_fallback_producao

router = APIRouter()

@router.get("/producao/{ano}")
def get_producao(ano: int):
    url = url_producao(ano)
    try:
        tabela = get_html_table(url)
        dados = parse_producao_html(tabela, ano)
        return {"dados": dados, "fonte": "scraper"}
    except Exception:
        fallback_data = get_fallback_producao(ano)
        return {"dados": fallback_data, "fonte": "fallback"}
    
def url_producao(ano: int) -> str:
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"