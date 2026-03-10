from fastapi import APIRouter, HTTPException
from app.controllers.programa_controller import *
from app.models.programa_model import Programa

router = APIRouter(prefix="/programas", tags=["Programas"])

nuevo_programa = ProgramaController()


@router.post("/create_programa")
async def create_programa(programa: Programa):
    rpta = nuevo_programa.create_programa(programa)
    return rpta


@router.get("/get_programas_por_facultad/{id_facultad}")
async def get_programas_por_facultad(id_facultad: int):
    return programa_controller.get_programas_por_facultad(id_facultad)


@router.get("/get_programas/")
async def get_programas():
    rpta = nuevo_programa.get_programas()
    return rpta


@router.put("/{id_programa}")
def update_programa(id_programa: int, programa: Programa):
    return programa_controller.update_programa(id_programa, programa)


@router.delete("/{id_programa}")
def delete_programa(id_programa: int):
    return programa_controller.delete_programa(id_programa)

