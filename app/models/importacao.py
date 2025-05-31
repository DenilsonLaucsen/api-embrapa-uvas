from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

class ImportacaoDado(BaseModel):
    paises: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "Kg"
    valor: Optional[int]
    unidade_valor: Optional[str] = "USD"
    ano: int

class ImportacaoResponse(BaseModel):
    dados: List[ImportacaoDado]
    fonte: str

class TipoImportacaoEnum(str, Enum):
    VINHOS_DE_MESA = "vinhos de mesa"
    ESPUMANTES = "espumantes"
    UVAS_FRESCAS = "uvas frescas"
    UVAS_PASSAS = "uvas passas"
    SUCO_DE_UVA = "suco de uva"