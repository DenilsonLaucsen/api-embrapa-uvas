from fastapi import FastAPI
from app.routes import producao, processamento, comercializacao, importacao, exportacao

app = FastAPI()

app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)
