from pydantic import BaseModel
from typing import Optional

class ProcessamentoDado(BaseModel):
    cultivar: str
    quantidade: Optional[int]
    unidade_quantidade: Optional[str] = "Kg"
    ano: int
