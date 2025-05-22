from fastapi import APIRouter, Query
from app.services.scraper import get_html_table

router = APIRouter()

TIPOS_PROCESSAMENTO = {
    "viniferas": "subopt_01",
    "americanas_hibridas": "subopt_02",
    "mesa": "subopt_03",
    "sem_classificacao": "subopt_04"
}

@router.get("/processamento/{ano}")
def get_processamento(ano: int, tipo: str = Query(..., description="viniferas | americanas_hibridas | mesa | sem_classificacao")):
    try:
        url = url_processamento(ano, tipo)
        dados = get_html_table(url)
        return {"ano": ano, "tipo": tipo, "dados": dados}
    except Exception as e:
        return {"erro": str(e)}

def url_processamento(ano: int, tipo: str) -> str:
    subopcao = TIPOS_PROCESSAMENTO.get(tipo.lower())
    if not subopcao:
        raise ValueError("Tipo inválido. Use: viniferas, americanas_hibridas, mesa ou sem_classificacao.")
    
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao={subopcao}"