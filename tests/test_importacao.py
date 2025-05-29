from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

expected_data = {
  "tipo": "espumantes",
  "dados": [
    {
      "paises": "Africa do Sul",
      "quantidade": 7650,
      "unidade_quantidade": "Kg",
      "valor": 69382,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Alemanha",
      "quantidade": 322,
      "unidade_quantidade": "Kg",
      "valor": 5111,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Argentina",
      "quantidade": 839006,
      "unidade_quantidade": "Kg",
      "valor": 2765843,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Austrália",
      "quantidade": 3150,
      "unidade_quantidade": "Kg",
      "valor": 10474,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Áustria",
      "quantidade": 882,
      "unidade_quantidade": "Kg",
      "valor": 8833,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bermudas",
      "quantidade": 3,
      "unidade_quantidade": "Kg",
      "valor": 54,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bahamas",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bélgica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Brasil",
      "quantidade": 7,
      "unidade_quantidade": "Kg",
      "valor": 184,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bulgária",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Canada",
      "quantidade": 23,
      "unidade_quantidade": "Kg",
      "valor": 279,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Chile",
      "quantidade": 592991,
      "unidade_quantidade": "Kg",
      "valor": 1952709,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Croácia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cuba",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Emirados Árabes Unidos",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Eslovênia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Espanha",
      "quantidade": 3438264,
      "unidade_quantidade": "Kg",
      "valor": 9801916,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Estados Unidos",
      "quantidade": 259,
      "unidade_quantidade": "Kg",
      "valor": 10273,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "França",
      "quantidade": 1401753,
      "unidade_quantidade": "Kg",
      "valor": 20166147,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Geórgia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Granada",
      "quantidade": 2,
      "unidade_quantidade": "Kg",
      "valor": 40,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Grécia",
      "quantidade": 300,
      "unidade_quantidade": "Kg",
      "valor": 1757,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Hong Kong",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Hungria",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Indonésia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Irlanda",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Israel",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Itália",
      "quantidade": 952639,
      "unidade_quantidade": "Kg",
      "valor": 3533749,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Japão",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Luxemburgo",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "México",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Moldávia",
      "quantidade": 955,
      "unidade_quantidade": "Kg",
      "valor": 1165,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nova Zelândia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Países Baixos",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Panamá",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Peru",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Portugal",
      "quantidade": 95326,
      "unidade_quantidade": "Kg",
      "valor": 386265,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Reino Unido",
      "quantidade": 1507,
      "unidade_quantidade": "Kg",
      "valor": 28581,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Romênia",
      "quantidade": 743,
      "unidade_quantidade": "Kg",
      "valor": 3841,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suíça",
      "quantidade": 464,
      "unidade_quantidade": "Kg",
      "valor": 34430,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tunísia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Ucrânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Uruguai",
      "quantidade": 10814,
      "unidade_quantidade": "Kg",
      "valor": 45704,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Não consta na tabela",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Não declarados",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Outros",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    }
  ],
  "fonte": "fallback"
}

def test_get_importacao_fallback():
    ano = 2023
    tipo = "espumantes"
    fallback_result = expected_data

    with patch("app.routes.importacao.get_html_table", side_effect=Exception("Erro simulado")):
        
        response = client.get(f"/importacao/{ano}?tipo={tipo}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["fonte"] == "fallback"
        assert json_data == fallback_result