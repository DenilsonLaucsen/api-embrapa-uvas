import csv
import os
import io
from typing import List
from app.models.producao import ProducaoDado
from app.models.comercializacao import ComercializacaoDado
from app.models.processamento import ProcessamentoDado
from app.models.importacao import ImportacaoDado
from app.models.exportacao import ExportacaoDado
from app.constants import (
    VINIFERAS, AMERICANAS_HIBRIDAS, MESA,
    VINHOS_DE_MESA, ESPUMANTES, UVAS_FRESCAS, SUCO_DE_UVA, UVAS_PASSAS
)
from app.utils.conversao import try_parse_int

FALLBACK_PATH = "docs"

def fallback_producao(ano: int) -> List[ProducaoDado]:
    path = os.path.join(FALLBACK_PATH, "Producao.csv")
    dados = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            produto = row.get("produto")
            quantidade = try_parse_int(row.get(str(ano), ""))
            if produto:
                dados.append(ProducaoDado(produto=produto, quantidade=quantidade, ano=ano))
    return dados

def fallback_comercializacao(ano: int) -> List[ComercializacaoDado]:
    path = os.path.join(FALLBACK_PATH, "Comercio.csv")
    dados = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            produto = row.get("Produto")
            quantidade = try_parse_int(row.get(str(ano), ""))
            if produto:
                dados.append(ComercializacaoDado(produto=produto, quantidade=quantidade, ano=ano))
    return dados

def fallback_processamento(ano: int, tipo: str) -> List[ProcessamentoDado]:
    nome_map = {
        VINIFERAS: "ProcessaViniferas.csv",
        AMERICANAS_HIBRIDAS: "ProcessaAmericanas.csv",
        MESA: "ProcessaMesa.csv",
    }

    path = os.path.join(FALLBACK_PATH, nome_map[tipo])
    dados = []

    with open(path, encoding="utf-8") as f:
        content = f.read()

    if "\\t" in content:
        content = content.replace("\\t", ";")
    elif "\t" in content:
        content = content.replace("\t", ";")
    elif ";" not in content:
        raise ValueError("Delimitador não identificado no arquivo CSV.")

    f = io.StringIO(content)
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        cultivar = row.get("cultivar")
        quantidade = try_parse_int(row.get(str(ano), ""))
        if cultivar:
            dados.append(ProcessamentoDado(cultivar=cultivar, quantidade=quantidade, ano=ano))

    return dados

def fallback_importacao(ano: int, tipo: str) -> List[ImportacaoDado]:
    nome_map = {
        VINHOS_DE_MESA: "ImpVinhos.csv",
        ESPUMANTES: "ImpEspumantes.csv",
        UVAS_FRESCAS: "ImpFrescas.csv",
        UVAS_PASSAS: "ImpPassas.csv",
        SUCO_DE_UVA: "ImpSuco.csv"
    }

    path = os.path.join(FALLBACK_PATH, nome_map[tipo])
    dados = []

    with open(path, encoding="utf-8") as f:
        content = f.read()

    if "\\t" in content:
        content = content.replace("\\t", ";")
    elif "\t" in content:
        content = content.replace("\t", ";")
    elif ";" not in content:
        raise ValueError("Delimitador não identificado no arquivo CSV.")

    f = io.StringIO(content)
    reader = csv.reader(f, delimiter=";")
    headers = next(reader)

    ano_str = str(ano)
    indices_ano = [i for i, h in enumerate(headers) if h == ano_str]

    if len(indices_ano) < 2:
        raise ValueError(f"Colunas de quantidade e valor para o ano {ano} não encontradas.")
    
    idx_quantidade, idx_valor = indices_ano[0], indices_ano[1]
    idx_pais = headers.index("País")

    for row in reader:
        if len(row) <= max(idx_pais, idx_quantidade, idx_valor):
            continue
        pais = row[idx_pais].strip()
        quantidade = try_parse_int(row[idx_quantidade])
        valor = try_parse_int(row[idx_valor])
        if pais:
            dados.append(ImportacaoDado(
                paises=pais,
                quantidade=quantidade,
                valor=valor,
                ano=ano
            ))

    return dados

def fallback_exportacao(ano: int, tipo: str) -> List[ExportacaoDado]:
    nome_map = {
        VINHOS_DE_MESA: "ExpVinho.csv",
        ESPUMANTES: "ExpEspumantes.csv",
        SUCO_DE_UVA: "ExpSuco.csv",
        UVAS_FRESCAS: "ExpUva.csv"
    }

    path = os.path.join(FALLBACK_PATH, nome_map[tipo])
    dados = []

    with open(path, encoding="utf-8") as f:
        content = f.read()

    if "\\t" in content:
        content = content.replace("\\t", ";")
    elif "\t" in content:
        content = content.replace("\t", ";")
    elif ";" not in content:
        raise ValueError("Delimitador não identificado no arquivo CSV.")

    f = io.StringIO(content)
    reader = csv.reader(f, delimiter=";")
    headers = next(reader)

    ano_str = str(ano)
    indices_ano = [i for i, h in enumerate(headers) if h == ano_str]

    if len(indices_ano) < 2:
        raise ValueError(f"Colunas de quantidade e valor para o ano {ano} não encontradas.")
    
    idx_quantidade, idx_valor = indices_ano[0], indices_ano[1]
    idx_pais = headers.index("País")

    for row in reader:
        if len(row) <= max(idx_pais, idx_quantidade, idx_valor):
            continue
        pais = row[idx_pais].strip()
        quantidade = try_parse_int(row[idx_quantidade])
        valor = try_parse_int(row[idx_valor])
        if pais:
            dados.append(ExportacaoDado(
                paises=pais,
                quantidade=quantidade,
                valor=valor,
                ano=ano
            ))

    return dados
    
def get_fallback_producao(ano: int):
    return fallback_producao(ano)

def get_fallback_comercializacao(ano: int):
    return fallback_comercializacao(ano)


def get_fallback_processa_viniferas(ano: int):
    return fallback_processamento(ano, VINIFERAS)

def get_fallback_processa_americanas(ano: int):
    return fallback_processamento(ano, AMERICANAS_HIBRIDAS)

def get_fallback_processa_mesa(ano: int):
    return fallback_processamento(ano, MESA)


def get_fallback_exp_vinhos(ano: int):
    return fallback_exportacao(ano, VINHOS_DE_MESA)

def get_fallback_exp_espumantes(ano: int):
    return fallback_exportacao(ano, ESPUMANTES)

def get_fallback_exp_uva(ano: int):
    return fallback_exportacao(ano, UVAS_FRESCAS)

def get_fallback_exp_suco(ano: int):
    return fallback_exportacao(ano, SUCO_DE_UVA)


def get_fallback_imp_vinhos(ano: int):
    return fallback_importacao(ano, VINHOS_DE_MESA)

def get_fallback_imp_espumantes(ano: int):
    return fallback_importacao(ano, ESPUMANTES)

def get_fallback_imp_frescas(ano: int):
    return fallback_importacao(ano, UVAS_FRESCAS)

def get_fallback_imp_passas(ano: int):
    return fallback_importacao(ano, UVAS_PASSAS)

def get_fallback_imp_suco(ano: int):
    return fallback_importacao(ano, SUCO_DE_UVA)
