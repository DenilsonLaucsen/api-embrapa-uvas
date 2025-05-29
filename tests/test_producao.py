from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

expected_data = {
  "dados": [
    {
      "produto": "VINHO DE MESA",
      "quantidade": 169762429,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Tinto",
      "quantidade": 139320884,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Branco",
      "quantidade": 27910299,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Rosado",
      "quantidade": 2531246,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "VINHO FINO DE MESA (VINIFERA)",
      "quantidade": 46268556,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Tinto",
      "quantidade": 23615783,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Branco",
      "quantidade": 20693437,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Rosado",
      "quantidade": 1959336,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "SUCO",
      "quantidade": 67045238,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Suco de uva integral",
      "quantidade": 38122173,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Suco de uva concentrado",
      "quantidade": 28216760,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Suco de uva adoçado",
      "quantidade": 94587,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Suco de uva orgânico",
      "quantidade": 611718,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Suco de uva reconstituído",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "DERIVADOS",
      "quantidade": 174716647,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Espumante",
      "quantidade": 65525,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Espumante moscatel",
      "quantidade": 14744,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Base espumante",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Base espumante moscatel",
      "quantidade": 6734590,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Base Champenoise champanha",
      "quantidade": 1552243,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Base Charmat champanha",
      "quantidade": 5418118,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Bebida de uva",
      "quantidade": 1627,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Polpa de uva",
      "quantidade": 1388251,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mosto simples",
      "quantidade": 157848983,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mosto concentrado",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mosto de uva com bagaço",
      "quantidade": 7784,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mosto dessulfitado",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mistelas",
      "quantidade": 600,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Néctar de uva",
      "quantidade": 70976,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Licorosos",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Compostos",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Jeropiga",
      "quantidade": 4500,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Filtrado",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Frisante",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinho leve",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinho licoroso",
      "quantidade": 73600,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Brandy",
      "quantidade": 450,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Destilado",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Bagaceira",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Licor de bagaceira",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinagre",
      "quantidade": 9000,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Borra líquida",
      "quantidade": 758140,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Borra seca",
      "quantidade": 17200,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinho Composto",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Pisco",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinho orgânico",
      "quantidade": 94150,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Espumante orgânico",
      "quantidade": 1365,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Destilado alcoólico simples de bagaceira",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Vinho acidificado",
      "quantidade": 2500,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Mosto parcialmente fermentado",
      "quantidade": 0,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Outros derivados",
      "quantidade": 652301,
      "unidade_quantidade": "L.",
      "ano": 2023
    },
    {
      "produto": "Total",
      "quantidade": 457792870,
      "unidade_quantidade": "L.",
      "ano": 2023
    }
  ],
  "fonte": "scraper"
}

def test_get_producao_exception_fallback():
    ano = 2023
    fallback_result = expected_data["dados"]

    with patch("app.routes.producao.get_html_table", side_effect=Exception("Erro simulado")), \
         patch("app.routes.producao.get_fallback_producao", return_value=expected_data["dados"]):
        
        response = client.get(f"/producao/{ano}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["fonte"] == "fallback"
        assert json_data["dados"] == fallback_result

def test_get_producao_scraper():
    ano = 2023

    response = client.get(f"/producao/{ano}")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["fonte"] == "scraper"
    assert json_data == expected_data