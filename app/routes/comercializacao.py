from fastapi import APIRouter
from app.services.scraper import get_html_table

router = APIRouter()

@router.get("/comercializacao/{ano}")
def get_processamento(ano: int):
    url = url_comercializacao(ano)
    try:
        dados = get_html_table(url)
        return {"ano": ano, "dados": dados}
    except Exception as e:
        return {"erro": str(e)}
    
def url_comercializacao(ano: int) -> str:
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"