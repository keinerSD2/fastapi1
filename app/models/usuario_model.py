from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id_usuario: Optional[int] = None
    primer_nombre: str
    primer_apellido: str
    telefono: str
    email: str
    password: str
    estado: bool
    id_rol: int

