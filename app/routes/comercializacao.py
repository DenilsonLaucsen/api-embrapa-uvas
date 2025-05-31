from fastapi import APIRouter, Path
from app.services.scraper import get_html_table, parse_comercializacao_html
from app.services.fallback import get_fallback_comercializacao
from app.models.comercializacao import ComercializacaoResponse

router = APIRouter()

@router.get("/comercializacao/{ano}", response_model=ComercializacaoResponse)
def get_processamento(
    ano: int = Path(..., description="Ano para o qual os dados de comercialização devem ser retornados", ge=1970, le=2023)
):
    """
    Retorna os dados de comercialização do ano fornecido.

    Se ocorrer uma falha ao acessar os dados online, um fallback será utilizado.
    """
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