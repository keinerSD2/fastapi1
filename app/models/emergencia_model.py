from pydantic import BaseModel
import datetime
from typing import Optional

class Emergencia(BaseModel):
    id_emergencia: Optional[int] = None
    id_usuario: int
    id_estudiante: int

    fecha: datetime.datetime
    descripcion: str
    atencion_prestada: str

