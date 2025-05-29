from fastapi import APIRouter
from app.services.scraper import get_html_table, parse_comercializacao_html
from app.services.fallback import get_fallback_comercializacao

router = APIRouter()

@router.get("/comercializacao/{ano}")
def get_processamento(ano: int):
    url = url_comercializacao(ano)
    try:
        tabela = get_html_table(url)
        dados = parse_comercializacao_html(tabela, ano)
        return {"dados": dados, "fonte": "scraper"}
    except Exception as e:
        dados = get_fallback_comercializacao(ano)
        return {"dados": dados, "fonte": "fallback"}
    
def url_comercializacao(ano: int) -> str:
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"