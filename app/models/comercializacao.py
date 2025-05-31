from pydantic import BaseModel
from typing import Optional, List

class ComercializacaoDado(BaseModel):
    produto: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "L."
    ano: int

class ComercializacaoResponse(BaseModel):
    dados: List[ComercializacaoDado]
    fonte: str