from pydantic import BaseModel
from typing import Optional
class Rol(BaseModel):
    id_rol: Optional[int] = None
    nombre: str
    descripcion: str
    acceso_privilegiado: bool

