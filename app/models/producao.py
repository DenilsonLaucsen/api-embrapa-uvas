from pydantic import BaseModel
from typing import List, Optional

class ProducaoDado(BaseModel):
    produto: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "L."
    ano: int

class ProducaoResponse(BaseModel):
    dados: List[ProducaoDado]
    fonte: str