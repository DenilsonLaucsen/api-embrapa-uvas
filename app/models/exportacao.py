from pydantic import BaseModel
from typing import Optional

class ExportacaoDado(BaseModel):
    paises: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "Kg"
    valor: Optional[int]
    unidade_valor: Optional[str] = "USD"
    ano: int
