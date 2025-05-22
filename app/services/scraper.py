import requests
from bs4 import BeautifulSoup

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