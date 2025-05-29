from pydantic import BaseModel
from typing import Optional

class ComercializacaoDado(BaseModel):
    produto: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "L."
    ano: int
