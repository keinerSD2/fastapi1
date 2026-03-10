from pydantic import BaseModel
from typing import Optional

class Facultad(BaseModel):
    id_facultad: Optional[int] = None
    nombre: str
    descripcion: str

