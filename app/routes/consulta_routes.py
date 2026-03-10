from fastapi import APIRouter, HTTPException
from app.controllers.consulta_controller import *
from app.models.consulta_model import Consulta

router = APIRouter(prefix="/consultas", tags=["Consultas"])

nueva_consulta = ConsultaController()


@router.post("/create_consulta")
async def create_consulta(consulta: Consulta):
    rpta = nueva_consulta.create_consulta(consulta)
    return rpta


@router.get("/get_consulta/{id_consulta}", response_model=Consulta)
async def get_consulta(id_consulta: int):
    rpta = nueva_consulta.get_consulta(id_consulta)
    return rpta

@router.get("/get_consultas_estudiante/{id_estudiante}")
async def get_consultas_estudiante(id_estudiante: int):
    rpta = nueva_consulta.get_consultas_estudiante(id_estudiante)
    return rpta


@router.get("/get_consultas/")
async def get_consultas():
    rpta = nueva_consulta.get_consultas()
    return rpta


@router.put("/{id_consulta}")
def update_consulta(id_consulta: int, consulta: Consulta):
    return consulta_controller.update_consulta(id_consulta, consulta)


@router.delete("/{id_consulta}")
def delete_consulta(id_consulta: int):
    return consulta_controller.delete_consulta(id_consulta)

