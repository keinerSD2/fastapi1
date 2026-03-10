from pydantic import BaseModel
from typing import Optional
class Programa(BaseModel):
    id_programa: Optional[int] = None
    id_facultad: int
    nombre: str
    descripcion: str

