from fastapi import APIRouter, Path
from app.services.scraper import get_html_table, parse_producao_html
from app.services.fallback import get_fallback_producao
from app.models.producao import ProducaoResponse

router = APIRouter()

@router.get("/producao/{ano}", response_model=ProducaoResponse)
def get_producao(
    ano: int = Path(..., description="Ano para o qual os dados de produção devem ser retornados", ge=1970, le=2023)
):
    """
    Retorna os dados de produção do ano fornecido.

    Se ocorrer uma falha ao acessar os dados online, um fallback será utilizado.
    """
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