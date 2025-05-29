import requests
from bs4 import BeautifulSoup
from app.models.producao import ProducaoDado
from app.models.processamento import ProcessamentoDado
from app.models.comercializacao import ComercializacaoDado
from app.models.exportacao import ExportacaoDado
from app.models.importacao import ImportacaoDado
from app.utils.conversao import try_parse_int

def get_html_table(url: str) -> list[dict]:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table", class_="tb_base tb_dados")

    if not table:
        raise ValueError("Tabela não encontrada.")

    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    data = []
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        values = [col.get_text(strip=True) for col in cols]
        if len(values) == len(headers):
            data.append(dict(zip(headers, values)))

    return data

def parse_producao_html(tabela: list[dict], ano: int) -> list[ProducaoDado]:
    result = []
    for row in tabela:
        produto = row.get("Produto")
        valor_str = row.get("Quantidade (L.)")
        quantidade = try_parse_int(valor_str)
        if produto:
            result.append(ProducaoDado(produto=produto, quantidade=quantidade, ano=ano))
    return result

def parse_processamento_html(tabela: list[dict], ano: int) -> list[ProcessamentoDado]:
    result = []
    for row in tabela:
        cultivar = row.get("Cultivar")
        valor_str = row.get("Quantidade (Kg)")
        quantidade = try_parse_int(valor_str)
        if cultivar:
            result.append(ProcessamentoDado(cultivar=cultivar, quantidade=quantidade, ano=ano))
    return result

def parse_comercializacao_html(tabela: list[dict], ano: int) -> list[ComercializacaoDado]:
    result = []
    for row in tabela:
        produto = row.get("Produto")
        valor_str = row.get("Quantidade (L.)")
        quantidade = try_parse_int(valor_str)
        if produto:
            result.append(ComercializacaoDado(produto=produto, quantidade=quantidade, ano=ano))
    return result

def parse_exportacao_html(tabela: list[dict], ano: int) -> list[ExportacaoDado]:
    result = []
    for row in tabela:
        paises = row.get("Países")
        quantidade_str = row.get("Quantidade (Kg)")
        valor_str = row.get("Valor (US$)")
        quantidade = try_parse_int(quantidade_str)
        valor = try_parse_int(valor_str)
        if paises:
            result.append(ExportacaoDado(paises=paises, quantidade=quantidade, valor=valor, ano=ano))
    return result

def parse_importacao_html(tabela: list[dict], ano: int) -> list[ImportacaoDado]:
    result = []
    for row in tabela:
        paises = row.get("Países")
        quantidade_str = row.get("Quantidade (Kg)")
        valor_str = row.get("Valor (US$)")
        quantidade = try_parse_int(quantidade_str)
        valor = try_parse_int(valor_str)
        if paises:
            result.append(ImportacaoDado(paises=paises, quantidade=quantidade, valor=valor, ano=ano))
    return result