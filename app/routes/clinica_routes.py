from fastapi import APIRouter, HTTPException
from app.controllers.clinica_controller import *
from app.models.clinica_model import Clinica

router = APIRouter(prefix="/clinicas", tags=["Clinicas"])

nueva_clinica = ClinicaController()


@router.post("/create_clinica")
async def create_clinica(clinica: Clinica):
    rpta = nueva_clinica.create_clinica(clinica)
    return rpta


@router.get("/get_clinica/{id_clinica}", response_model=Clinica)
async def get_clinica(id_clinica: int):
    rpta = nueva_clinica.get_clinica(id_clinica)
    return rpta


@router.get("/get_clinicas/")
async def get_clinicas():
    rpta = nueva_clinica.get_clinicas()
    return rpta


@router.put("/{id_clinica}")
def update_clinica(id_clinica: int, clinica: Clinica):
    return clinica_controller.update_clinica(id_clinica, clinica)


@router.delete("/{id_clinica}")
def delete_clinica(id_clinica: int):
    return clinica_controller.delete_clinica(id_clinica)
