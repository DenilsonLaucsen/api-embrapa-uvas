from fastapi import APIRouter
from app.services.scraper import get_html_table

router = APIRouter()

@router.get("/producao/{ano}")
def get_producao(ano: int):
    url = url_producao(ano)
    try:
        dados = get_html_table(url)
        return {"ano": ano, "dados": dados}
    except Exception as e:
        return {"erro": str(e)}
    
def url_producao(ano: int) -> str:
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"