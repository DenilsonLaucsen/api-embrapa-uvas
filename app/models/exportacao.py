from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

class ExportacaoDado(BaseModel):
    paises: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "Kg"
    valor: Optional[int]
    unidade_valor: Optional[str] = "USD"
    ano: int

class ExportacaoResponse(BaseModel):
    dados: List[ExportacaoDado]
    fonte: str

class TipoExportacaoEnum(str, Enum):
    VINHOS_DE_MESA = "vinhos de mesa"
    ESPUMANTES = "espumantes"
    UVAS_FRESCAS = "uvas frescas"
    SUCO_DE_UVA = "suco de uva"