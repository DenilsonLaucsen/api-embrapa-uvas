from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

class ProcessamentoDado(BaseModel):
    cultivar: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "Kg"
    ano: int

class ProcessamentoResponse(BaseModel):
    dados: List[ProcessamentoDado]
    fonte: str

class TipoProcessamentoEnum(str, Enum):
    VINIFERAS = "viníferas"
    AMERICANAS_HIBRIDAS = "americanas e híbridas"
    MESA = "mesa"
    SEM_CLASSIFICACAO = "sem classificação"