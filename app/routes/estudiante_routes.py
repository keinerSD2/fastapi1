from fastapi import APIRouter, HTTPException
from app.controllers.estudiante_controller import *
from app.models.estudiante_model import Estudiante

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

nuevo_estudiante = EstudianteController()


@router.post("/create_estudiante")
async def create_estudiante(estudiante: Estudiante):
    rpta = nuevo_estudiante.create_estudiante(estudiante)
    return rpta


@router.get("/get_estudiante/{numero_identificacion}", response_model=Estudiante)
async def get_estudiante(numero_identificacion: int):
    rpta = nuevo_estudiante.get_estudiante(numero_identificacion)
    return rpta


@router.get("/get_estudiantes/")
async def get_estudiantes():
    rpta = nuevo_estudiante.get_estudiantes()
    return rpta


@router.put("/{id_estudiante}")
def update_estudiante(id_estudiante: int, estudiante: Estudiante):
    return estudiante_controller.update_estudiante(id_estudiante, estudiante)


@router.delete("/{id_estudiante}")
def delete_estudiante(id_estudiante: int):
    return estudiante_controller.delete_estudiante(id_estudiante)


