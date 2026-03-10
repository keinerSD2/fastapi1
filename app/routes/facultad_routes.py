from fastapi import APIRouter, HTTPException
from app.controllers.facultad_controller import *
from app.models.facultad_model import Facultad

router = APIRouter(prefix="/facultades", tags=["Facultades"])

nueva_facultad = FacultadController()


@router.post("/create_facultad")
async def create_facultad(facultad: Facultad):
    rpta = nueva_facultad.create_facultad(facultad)
    return rpta


@router.get("/get_facultad/{id_facultad}", response_model=Facultad)
async def get_facultad(id_facultad: int):
    rpta = nueva_facultad.get_facultad(id_facultad)
    return rpta


@router.get("/get_facultades/")
async def get_facultades():
    rpta = nueva_facultad.get_facultades()
    return rpta


@router.put("/{id_facultad}")
def update_facultad(id_facultad: int, facultad: Facultad):
    return facultad_controller.update_facultad(id_facultad, facultad)


@router.delete("/{id_facultad}")
def delete_facultad(id_facultad: int):
    return facultad_controller.delete_facultad(id_facultad)
