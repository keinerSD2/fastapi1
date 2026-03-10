from fastapi import APIRouter, HTTPException
from app.controllers.emergencia_controller import *
from app.models.emergencia_model import Emergencia

router = APIRouter(prefix="/emergencias", tags=["Emergencias"])

nueva_emergencia = EmergenciaController()


@router.post("/create_emergencia")
async def create_emergencia(emergencia: Emergencia):
    rpta = nueva_emergencia.create_emergencia(emergencia)
    return rpta


@router.get("/get_emergencia/{id_emergencia}", response_model=Emergencia)
async def get_emergencia(id_emergencia: int):
    rpta = nueva_emergencia.get_emergencia(id_emergencia)
    return rpta


@router.get("/get_emergencias/")
async def get_emergencias():
    rpta = nueva_emergencia.get_emergencias()
    return rpta


@router.put("/{id_emergencia}")
def update_emergencia(id_emergencia: int, emergencia: Emergencia):
    return emergencia_controller.update_emergencia(id_emergencia, emergencia)


@router.delete("/{id_emergencia}")
def delete_emergencia(id_emergencia: int):
    return emergencia_controller.delete_emergencia(id_emergencia)
