from pydantic import BaseModel
import datetime
from typing import Optional

class Estudiante(BaseModel):
    id_estudiante: Optional[int] = None
    id_facultad: Optional[int]
    id_programa: Optional[int]
    id_usuario: Optional[int]

    primer_nombre: str
    primer_apellido: str
    tipo_identificacion: str
    numero_identificacion: int
    genero: str
    telefono: Optional[int]
    direccion: Optional[str]

    fecha_registro: Optional[datetime.datetime]


