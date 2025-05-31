# 🍇 api-embrapa-uvas

API para consulta de dados públicos da vitivinicultura brasileira, com base nas informações disponibilizadas pela Embrapa.

---

## 📌 Objetivo

Este projeto faz parte do Tech Challenge da pós-graduação em Machine Learning Engineering. O objetivo é criar uma API que consulte e disponibilize os dados das seguintes abas do site da Embrapa:

- Produção  
- Processamento  
- Comercialização  
- Importação  
- Exportação  

---

## 🚀 Stack utilizada

O projeto foi desenvolvido com foco em simplicidade, desempenho e facilidade de uso:

- **Python 3.11**
- **FastAPI** – Criação dos endpoints RESTful.
- **BeautifulSoup** – Web scraping das tabelas públicas do site da Embrapa.
- **Requests / HTTPX** – Requisições HTTP.
- **Pytest** – Testes automatizados.
- **Uvicorn** – Servidor ASGI para execução local.

---

## 🧭 Funcionalidades esperadas

- Consulta automática ao site da Embrapa.
- Fallback local para uso offline ou indisponibilidade do site.
- Endpoints organizados por tipo de dado.
- Documentação acessível para uso da API.
- Possibilidade de execução local e testes automatizados.

---

## ⚙️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/DenilsonLaucsen/api-embrapa-uvas.git
cd api-embrapa-uvas
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```
#### Ativação no Windows
```bash
venv\Scripts\activate
```
#### Ativação no Linux/Mac
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: http://localhost:8000
Documentação automática: http://localhost:8000/docs

---

### 🧪 Como rodar os testes

```bash
pytest
```

---

### 📺 Demonstração em vídeo
Confira a demonstração do projeto no link abaixo:


## 📊 Diagrama de Arquitetura

Abaixo está uma visão geral de alto nível da arquitetura do projeto:

![Diagrama de Arquitetura](docs/architecture-diagram.png)

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT.
