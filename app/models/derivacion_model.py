from pydantic import BaseModel
import datetime
from typing import Optional

class Derivacion(BaseModel):
    id_derivacion: Optional[int] = None
    id_consulta: int
    id_clinica: int

    razon: str
    fecha: datetime.datetime

