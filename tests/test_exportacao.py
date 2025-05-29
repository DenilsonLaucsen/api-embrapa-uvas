from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

expected_data = {
  "dados_scraper": [
    {
      "paises": "Afeganistão",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "África do Sul",
      "quantidade": 117,
      "unidade_quantidade": "Kg",
      "valor": 698,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Alemanha, República Democrática",
      "quantidade": 4806,
      "unidade_quantidade": "Kg",
      "valor": 31853,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Angola",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Anguilla",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Antígua e Barbuda",
      "quantidade": 383,
      "unidade_quantidade": "Kg",
      "valor": 1848,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Antilhas Holandesas",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Arábia Saudita",
      "quantidade": 124,
      "unidade_quantidade": "Kg",
      "valor": 142,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Argélia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Argentina",
      "quantidade": 4545,
      "unidade_quantidade": "Kg",
      "valor": 36133,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Aruba",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Austrália",
      "quantidade": 2485,
      "unidade_quantidade": "Kg",
      "valor": 13565,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Áustria",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bahamas",
      "quantidade": 1348,
      "unidade_quantidade": "Kg",
      "valor": 7402,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bangladesh",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Barbados",
      "quantidade": 58,
      "unidade_quantidade": "Kg",
      "valor": 303,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Barein",
      "quantidade": 283,
      "unidade_quantidade": "Kg",
      "valor": 1684,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bélgica",
      "quantidade": 95,
      "unidade_quantidade": "Kg",
      "valor": 683,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Belice",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Benin",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bermudas",
      "quantidade": 16,
      "unidade_quantidade": "Kg",
      "valor": 153,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bolívia",
      "quantidade": 21926,
      "unidade_quantidade": "Kg",
      "valor": 36950,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bósnia-Herzegovina",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Brasil",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Cabo Verde",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Camarões",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Canadá",
      "quantidade": 11539,
      "unidade_quantidade": "Kg",
      "valor": 42179,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Catar",
      "quantidade": 5,
      "unidade_quantidade": "Kg",
      "valor": 18,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cayman, Ilhas",
      "quantidade": 438,
      "unidade_quantidade": "Kg",
      "valor": 2632,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Chile",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 63,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "China",
      "quantidade": 73917,
      "unidade_quantidade": "Kg",
      "valor": 183096,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Chipre",
      "quantidade": 524,
      "unidade_quantidade": "Kg",
      "valor": 2995,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cingapura",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cocos (Keeling), Ilhas",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Colômbia",
      "quantidade": 450,
      "unidade_quantidade": "Kg",
      "valor": 1259,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Comores",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Congo",
      "quantidade": 17100,
      "unidade_quantidade": "Kg",
      "valor": 26600,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Coreia, Republica Sul",
      "quantidade": 25,
      "unidade_quantidade": "Kg",
      "valor": 171,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Costa do Marfim",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Costa Rica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Coveite (Kuweit)",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Curaçao",
      "quantidade": 25135,
      "unidade_quantidade": "Kg",
      "valor": 40807,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Dinamarca",
      "quantidade": 1734,
      "unidade_quantidade": "Kg",
      "valor": 15261,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Dominica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "El Salvador",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Emirados Arabes Unidos",
      "quantidade": 1417,
      "unidade_quantidade": "Kg",
      "valor": 6762,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Equador",
      "quantidade": 2790,
      "unidade_quantidade": "Kg",
      "valor": 4392,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Eslovaca, Republica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Espanha",
      "quantidade": 180,
      "unidade_quantidade": "Kg",
      "valor": 4171,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Estados Unidos",
      "quantidade": 229839,
      "unidade_quantidade": "Kg",
      "valor": 429091,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Estônia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Filipinas",
      "quantidade": 94,
      "unidade_quantidade": "Kg",
      "valor": 334,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Finlândia",
      "quantidade": 5,
      "unidade_quantidade": "Kg",
      "valor": 11,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "França",
      "quantidade": 2265,
      "unidade_quantidade": "Kg",
      "valor": 14722,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gabão",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gana",
      "quantidade": 7237,
      "unidade_quantidade": "Kg",
      "valor": 29473,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gibraltar",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Granada",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Grécia",
      "quantidade": 1294,
      "unidade_quantidade": "Kg",
      "valor": 3214,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guatemala",
      "quantidade": 2053,
      "unidade_quantidade": "Kg",
      "valor": 3758,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guiana",
      "quantidade": 33651,
      "unidade_quantidade": "Kg",
      "valor": 88715,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guiana Francesa",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guine Bissau",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guine Equatorial",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Haiti",
      "quantidade": 559645,
      "unidade_quantidade": "Kg",
      "valor": 871661,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Honduras",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Hong Kong",
      "quantidade": 16255,
      "unidade_quantidade": "Kg",
      "valor": 71025,
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
      "paises": "Ilha de Man",
      "quantidade": 1428,
      "unidade_quantidade": "Kg",
      "valor": 4533,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Ilhas Virgens",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Índia",
      "quantidade": 60,
      "unidade_quantidade": "Kg",
      "valor": 170,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Indonésia",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 30,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Irã",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Iraque",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Irlanda",
      "quantidade": 150,
      "unidade_quantidade": "Kg",
      "valor": 377,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Itália",
      "quantidade": 2922,
      "unidade_quantidade": "Kg",
      "valor": 27665,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Jamaica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Japão",
      "quantidade": 22942,
      "unidade_quantidade": "Kg",
      "valor": 57780,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Jordânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Letônia",
      "quantidade": 8,
      "unidade_quantidade": "Kg",
      "valor": 8,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Líbano",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Libéria",
      "quantidade": 39784,
      "unidade_quantidade": "Kg",
      "valor": 42463,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Luxemburgo",
      "quantidade": 581,
      "unidade_quantidade": "Kg",
      "valor": 7048,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Macau",
      "quantidade": 7,
      "unidade_quantidade": "Kg",
      "valor": 6,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malásia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malavi",
      "quantidade": 3660,
      "unidade_quantidade": "Kg",
      "valor": 6252,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malta",
      "quantidade": 6561,
      "unidade_quantidade": "Kg",
      "valor": 24199,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Marshall, Ilhas",
      "quantidade": 7417,
      "unidade_quantidade": "Kg",
      "valor": 31691,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Martinica",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 31,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Mauritânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "México",
      "quantidade": 3,
      "unidade_quantidade": "Kg",
      "valor": 19,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Moçambique",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Montenegro",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Namíbia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nicarágua",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nigéria",
      "quantidade": 10800,
      "unidade_quantidade": "Kg",
      "valor": 16464,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Noruega",
      "quantidade": 861,
      "unidade_quantidade": "Kg",
      "valor": 4243,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nova Caledônia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nova Zelândia",
      "quantidade": 338,
      "unidade_quantidade": "Kg",
      "valor": 7177,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Omã",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Países Baixos",
      "quantidade": 2244,
      "unidade_quantidade": "Kg",
      "valor": 4958,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Palau",
      "quantidade": 45,
      "unidade_quantidade": "Kg",
      "valor": 143,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Panamá",
      "quantidade": 14785,
      "unidade_quantidade": "Kg",
      "valor": 68173,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Paraguai",
      "quantidade": 3780378,
      "unidade_quantidade": "Kg",
      "valor": 5517263,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Peru",
      "quantidade": 47277,
      "unidade_quantidade": "Kg",
      "valor": 84282,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Pitcairn",
      "quantidade": 11,
      "unidade_quantidade": "Kg",
      "valor": 22,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Polônia",
      "quantidade": 298,
      "unidade_quantidade": "Kg",
      "valor": 590,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Porto Rico",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Portugal",
      "quantidade": 13742,
      "unidade_quantidade": "Kg",
      "valor": 46311,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Quênia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Reino Unido",
      "quantidade": 11326,
      "unidade_quantidade": "Kg",
      "valor": 84547,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "República Dominicana",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Rússia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Cristóvão e Névis",
      "quantidade": 16,
      "unidade_quantidade": "Kg",
      "valor": 31,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Tomé e Príncipe",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Vicente e Granadinas",
      "quantidade": 39,
      "unidade_quantidade": "Kg",
      "valor": 139,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Senegal",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Serra Leoa",
      "quantidade": 23200,
      "unidade_quantidade": "Kg",
      "valor": 38548,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Sérvia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Singapura",
      "quantidade": 3941,
      "unidade_quantidade": "Kg",
      "valor": 19781,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suazilândia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suécia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suíça",
      "quantidade": 2500,
      "unidade_quantidade": "Kg",
      "valor": 28763,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suriname",
      "quantidade": 3105,
      "unidade_quantidade": "Kg",
      "valor": 5235,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tailândia",
      "quantidade": 189,
      "unidade_quantidade": "Kg",
      "valor": 1387,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Taiwan (Formosa)",
      "quantidade": 4208,
      "unidade_quantidade": "Kg",
      "valor": 19998,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tanzânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tcheca, República",
      "quantidade": 405,
      "unidade_quantidade": "Kg",
      "valor": 3348,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Togo",
      "quantidade": 14550,
      "unidade_quantidade": "Kg",
      "valor": 25235,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Toquelau",
      "quantidade": 3,
      "unidade_quantidade": "Kg",
      "valor": 10,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Trinidade Tobago",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Turquia",
      "quantidade": 28104,
      "unidade_quantidade": "Kg",
      "valor": 95421,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tuvalu",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Uruguai",
      "quantidade": 326093,
      "unidade_quantidade": "Kg",
      "valor": 454271,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Vanuatu",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Venezuela",
      "quantidade": 141030,
      "unidade_quantidade": "Kg",
      "valor": 220512,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Vietnã",
      "quantidade": 72,
      "unidade_quantidade": "Kg",
      "valor": 128,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Total",
      "quantidade": 5538888,
      "unidade_quantidade": "Kg",
      "valor": 8923076,
      "unidade_valor": "USD",
      "ano": 2023
    }
  ],
  "dados_fallback": [
          {
      "paises": "Afeganistão",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "África do Sul",
      "quantidade": 117,
      "unidade_quantidade": "Kg",
      "valor": 698,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Alemanha, República Democrática",
      "quantidade": 4806,
      "unidade_quantidade": "Kg",
      "valor": 31853,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Angola",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Anguilla",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Antígua e Barbuda",
      "quantidade": 383,
      "unidade_quantidade": "Kg",
      "valor": 1848,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Antilhas Holandesas",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Arábia Saudita",
      "quantidade": 124,
      "unidade_quantidade": "Kg",
      "valor": 142,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Argélia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Argentina",
      "quantidade": 4545,
      "unidade_quantidade": "Kg",
      "valor": 36133,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Aruba",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Austrália",
      "quantidade": 2485,
      "unidade_quantidade": "Kg",
      "valor": 13565,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Áustria",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bahamas",
      "quantidade": 1348,
      "unidade_quantidade": "Kg",
      "valor": 7402,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bangladesh",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Barbados",
      "quantidade": 58,
      "unidade_quantidade": "Kg",
      "valor": 303,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Barein",
      "quantidade": 283,
      "unidade_quantidade": "Kg",
      "valor": 1684,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bélgica",
      "quantidade": 95,
      "unidade_quantidade": "Kg",
      "valor": 683,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Belice",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Benin",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bermudas",
      "quantidade": 16,
      "unidade_quantidade": "Kg",
      "valor": 153,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bolívia",
      "quantidade": 21926,
      "unidade_quantidade": "Kg",
      "valor": 36950,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Bósnia-Herzegovina",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Brasil",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Cabo Verde",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Camarões",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Canadá",
      "quantidade": 11539,
      "unidade_quantidade": "Kg",
      "valor": 42179,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Catar",
      "quantidade": 5,
      "unidade_quantidade": "Kg",
      "valor": 18,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cayman, Ilhas",
      "quantidade": 438,
      "unidade_quantidade": "Kg",
      "valor": 2632,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Chile",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 63,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "China",
      "quantidade": 73917,
      "unidade_quantidade": "Kg",
      "valor": 183096,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Chipre",
      "quantidade": 524,
      "unidade_quantidade": "Kg",
      "valor": 2995,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cingapura",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Cocos (Keeling), Ilhas",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Colômbia",
      "quantidade": 450,
      "unidade_quantidade": "Kg",
      "valor": 1259,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Comores",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Congo",
      "quantidade": 17100,
      "unidade_quantidade": "Kg",
      "valor": 26600,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Coreia, Republica Sul",
      "quantidade": 25,
      "unidade_quantidade": "Kg",
      "valor": 171,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Costa do Marfim",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Costa Rica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Coveite (Kuweit)",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Curaçao",
      "quantidade": 25135,
      "unidade_quantidade": "Kg",
      "valor": 40807,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Dinamarca",
      "quantidade": 1734,
      "unidade_quantidade": "Kg",
      "valor": 15261,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Dominica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "El Salvador",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Emirados Arabes Unidos",
      "quantidade": 1417,
      "unidade_quantidade": "Kg",
      "valor": 6762,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Equador",
      "quantidade": 2790,
      "unidade_quantidade": "Kg",
      "valor": 4392,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Eslovaca, Republica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Espanha",
      "quantidade": 180,
      "unidade_quantidade": "Kg",
      "valor": 4171,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Estados Unidos",
      "quantidade": 229839,
      "unidade_quantidade": "Kg",
      "valor": 429091,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Estônia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Filipinas",
      "quantidade": 94,
      "unidade_quantidade": "Kg",
      "valor": 334,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Finlândia",
      "quantidade": 5,
      "unidade_quantidade": "Kg",
      "valor": 11,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "França",
      "quantidade": 2265,
      "unidade_quantidade": "Kg",
      "valor": 14722,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gabão",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gana",
      "quantidade": 7237,
      "unidade_quantidade": "Kg",
      "valor": 29473,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Gibraltar",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Granada",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Grécia",
      "quantidade": 1294,
      "unidade_quantidade": "Kg",
      "valor": 3214,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guatemala",
      "quantidade": 2053,
      "unidade_quantidade": "Kg",
      "valor": 3758,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guiana",
      "quantidade": 33651,
      "unidade_quantidade": "Kg",
      "valor": 88715,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guiana Francesa",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guine Bissau",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Guine Equatorial",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Haiti",
      "quantidade": 559645,
      "unidade_quantidade": "Kg",
      "valor": 871661,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Honduras",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Hong Kong",
      "quantidade": 16255,
      "unidade_quantidade": "Kg",
      "valor": 71025,
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
      "paises": "Ilha de Man",
      "quantidade": 1428,
      "unidade_quantidade": "Kg",
      "valor": 4533,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Ilhas Virgens",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Índia",
      "quantidade": 60,
      "unidade_quantidade": "Kg",
      "valor": 170,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Indonésia",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 30,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Irã",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Iraque",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Irlanda",
      "quantidade": 150,
      "unidade_quantidade": "Kg",
      "valor": 377,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Itália",
      "quantidade": 2922,
      "unidade_quantidade": "Kg",
      "valor": 27665,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Jamaica",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Japão",
      "quantidade": 22942,
      "unidade_quantidade": "Kg",
      "valor": 57780,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Jordânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Letônia",
      "quantidade": 8,
      "unidade_quantidade": "Kg",
      "valor": 8,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Líbano",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Libéria",
      "quantidade": 39784,
      "unidade_quantidade": "Kg",
      "valor": 42463,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Luxemburgo",
      "quantidade": 581,
      "unidade_quantidade": "Kg",
      "valor": 7048,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Macau",
      "quantidade": 7,
      "unidade_quantidade": "Kg",
      "valor": 6,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malásia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malavi",
      "quantidade": 3660,
      "unidade_quantidade": "Kg",
      "valor": 6252,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Malta",
      "quantidade": 6561,
      "unidade_quantidade": "Kg",
      "valor": 24199,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Marshall, Ilhas",
      "quantidade": 7417,
      "unidade_quantidade": "Kg",
      "valor": 31691,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Martinica",
      "quantidade": 9,
      "unidade_quantidade": "Kg",
      "valor": 31,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Mauritânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "México",
      "quantidade": 3,
      "unidade_quantidade": "Kg",
      "valor": 19,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Moçambique",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Montenegro",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Namíbia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nicarágua",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nigéria",
      "quantidade": 10800,
      "unidade_quantidade": "Kg",
      "valor": 16464,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Noruega",
      "quantidade": 861,
      "unidade_quantidade": "Kg",
      "valor": 4243,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nova Caledônia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Nova Zelândia",
      "quantidade": 338,
      "unidade_quantidade": "Kg",
      "valor": 7177,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Omã",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Países Baixos",
      "quantidade": 2244,
      "unidade_quantidade": "Kg",
      "valor": 4958,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Palau",
      "quantidade": 45,
      "unidade_quantidade": "Kg",
      "valor": 143,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Panamá",
      "quantidade": 14785,
      "unidade_quantidade": "Kg",
      "valor": 68173,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Paraguai",
      "quantidade": 3780378,
      "unidade_quantidade": "Kg",
      "valor": 5517263,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Peru",
      "quantidade": 47277,
      "unidade_quantidade": "Kg",
      "valor": 84282,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Pitcairn",
      "quantidade": 11,
      "unidade_quantidade": "Kg",
      "valor": 22,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Polônia",
      "quantidade": 298,
      "unidade_quantidade": "Kg",
      "valor": 590,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Porto Rico",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Portugal",
      "quantidade": 13742,
      "unidade_quantidade": "Kg",
      "valor": 46311,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Quênia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Reino Unido",
      "quantidade": 11326,
      "unidade_quantidade": "Kg",
      "valor": 84547,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "República Dominicana",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Rússia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Cristóvão e Névis",
      "quantidade": 16,
      "unidade_quantidade": "Kg",
      "valor": 31,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Tomé e Príncipe",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "São Vicente e Granadinas",
      "quantidade": 39,
      "unidade_quantidade": "Kg",
      "valor": 139,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Senegal",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Serra Leoa",
      "quantidade": 23200,
      "unidade_quantidade": "Kg",
      "valor": 38548,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Sérvia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Singapura",
      "quantidade": 3941,
      "unidade_quantidade": "Kg",
      "valor": 19781,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suazilândia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suécia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suíça",
      "quantidade": 2500,
      "unidade_quantidade": "Kg",
      "valor": 28763,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Suriname",
      "quantidade": 3105,
      "unidade_quantidade": "Kg",
      "valor": 5235,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tailândia",
      "quantidade": 189,
      "unidade_quantidade": "Kg",
      "valor": 1387,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Taiwan (Formosa)",
      "quantidade": 4208,
      "unidade_quantidade": "Kg",
      "valor": 19998,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tanzânia",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tcheca, República",
      "quantidade": 405,
      "unidade_quantidade": "Kg",
      "valor": 3348,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Togo",
      "quantidade": 14550,
      "unidade_quantidade": "Kg",
      "valor": 25235,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Toquelau",
      "quantidade": 3,
      "unidade_quantidade": "Kg",
      "valor": 10,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Trinidade Tobago",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
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
      "paises": "Turquia",
      "quantidade": 28104,
      "unidade_quantidade": "Kg",
      "valor": 95421,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Tuvalu",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Uruguai",
      "quantidade": 326093,
      "unidade_quantidade": "Kg",
      "valor": 454271,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Vanuatu",
      "quantidade": 0,
      "unidade_quantidade": "Kg",
      "valor": 0,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Venezuela",
      "quantidade": 141030,
      "unidade_quantidade": "Kg",
      "valor": 220512,
      "unidade_valor": "USD",
      "ano": 2023
    },
    {
      "paises": "Vietnã",
      "quantidade": 72,
      "unidade_quantidade": "Kg",
      "valor": 128,
      "unidade_valor": "USD",
      "ano": 2023
    }
  ]
}

def test_get_exportacao_exception_fallback():
    ano = 2023
    tipo = "vinhos_de_mesa"
    fallback_result = expected_data["dados_scraper"]

    with patch.dict("app.routes.exportacao.FALLBACK_FUNCS", {
        "vinhos_de_mesa": lambda ano: fallback_result
        }), patch("app.routes.exportacao.get_html_table", side_effect=Exception("Erro simulado")):
        
        response = client.get(f"/exportacao/{ano}?tipo={tipo}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["fonte"] == "fallback"
        assert json_data["dados"] == fallback_result

def test_get_exportacao_fallback():
    ano = 2023
    tipo = "vinhos_de_mesa"
    fallback_result = expected_data["dados_fallback"]

    with patch("app.routes.exportacao.get_html_table", side_effect=Exception("Erro simulado")):
        
        response = client.get(f"/exportacao/{ano}?tipo={tipo}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["fonte"] == "fallback"
        assert json_data["dados"] == fallback_result