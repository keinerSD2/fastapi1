from fastapi import APIRouter, HTTPException
from app.controllers.auth_controller import *
from app.models.auth_model import Login, Register

router = APIRouter()

nuevo_auth = AuthController()

@router.post("/login")
async def login(datos: Login):
    rpta = nuevo_auth.login(datos)
    return rpta

@router.post("/register")
async def register(datos: Register):
    rpta = nuevo_auth.register(datos)
    return rpta
