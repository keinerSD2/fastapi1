from fastapi import APIRouter, HTTPException
from app.controllers.derivacion_controller import *
from app.models.derivacion_model import Derivacion

router = APIRouter(prefix="/derivaciones", tags=["Derivaciones"])

nueva_derivacion = DerivacionController()


@router.post("/create_derivacion")
async def create_derivacion(derivacion: Derivacion):
    rpta = nueva_derivacion.create_derivacion(derivacion)
    return rpta


@router.get("/get_derivacion/{id_derivacion}", response_model=Derivacion)
async def get_derivacion(id_derivacion: int):
    rpta = nueva_derivacion.get_derivacion(id_derivacion)
    return rpta


@router.get("/get_derivaciones/")
async def get_derivaciones():
    rpta = nueva_derivacion.get_derivaciones()
    return rpta


@router.put("/{id_derivacion}")
def update_derivacion(id_derivacion: int, derivacion: Derivacion):
    return derivacion_controller.update_derivacion(id_derivacion, derivacion)


@router.delete("/{id_derivacion}")
def delete_derivacion(id_derivacion: int):
    return derivacion_controller.delete_derivacion(id_derivacion)
