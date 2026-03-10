from pydantic import BaseModel
from typing import Optional
class SignosVitales(BaseModel):
    id_signos: Optional[int] = None
    id_consulta: int

    presion_arterial: str
    temperatura: float
    peso: float
    altura: float
    saturacion_oxigeno: float
    frecuencia_cardiaca: float
    tipo_sangre: str


