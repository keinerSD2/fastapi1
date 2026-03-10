from pydantic import BaseModel
from typing import Optional

class Clinica(BaseModel):
    id_clinica: Optional[int] = None
    nombre: str
    ubicacion: str

