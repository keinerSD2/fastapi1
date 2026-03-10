from fastapi import APIRouter, HTTPException
from app.controllers.rol_controller import *
from app.models.rol_model import Rol

router = APIRouter(prefix="/roles", tags=["Roles"])

nuevo_rol = RolController()


@router.post("/create_rol")
async def create_rol(rol: Rol):
    rpta = nuevo_rol.create_rol(rol)
    return rpta


@router.get("/get_rol/{id_rol}", response_model=Rol)
async def get_rol(id_rol: int):
    rpta = nuevo_rol.get_rol(id_rol)
    return rpta


@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_rol.get_roles()
    return rpta


@router.put("/{id_rol}")
def update_rol(id_rol: int, rol: Rol):
    return rol_controller.update_rol(id_rol, rol)


@router.delete("/{id_rol}")
def delete_rol(id_rol: int):
    return rol_controller.delete_rol(id_rol)
