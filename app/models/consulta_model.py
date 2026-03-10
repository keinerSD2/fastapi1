from pydantic import BaseModel
import datetime
from typing import Optional

class Consulta(BaseModel):
    id_consulta: Optional[int] = None
    id_estudiante: int
    id_usuario: int

    diagnostico: str
    observaciones: str
    motivo_consulta: str

    fecha_entrada: datetime.datetime
    fecha_salida: datetime.datetime

