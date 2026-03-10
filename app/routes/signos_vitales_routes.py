from fastapi import APIRouter, HTTPException
from app.controllers.signos_vitales_controller import *
from app.models.signos_vitales_model import SignosVitales

router = APIRouter(prefix="/signos_vitales", tags=["Signos Vitales"])

nuevo_signos = SignosVitalesController()


@router.post("/create_signos")
async def create_signos(signos: SignosVitales):
    rpta = nuevo_signos.create_signos(signos)
    return rpta


@router.get("/get_signos/{id_signos}", response_model=SignosVitales)
async def get_signos(id_signos: int):
    rpta = nuevo_signos.get_signos(id_signos)
    return rpta


@router.get("/get_signos_all/")
async def get_signos_all():
    rpta = nuevo_signos.get_signos_all()
    return rpta


@router.put("/{id_signos}")
def update_signos(id_signos: int, signos: SignosVitales):
    return signos_vitales_controller.update_signos(id_signos, signos)


@router.delete("/{id_signos}")
def delete_signos(id_signos: int):
    return signos_vitales_controller.delete_signos(id_signos)
