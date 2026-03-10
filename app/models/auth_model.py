from pydantic import BaseModel

class Login(BaseModel):
    email: str
    password: str

class Register(BaseModel):
    primer_nombre: str
    primer_apellido: str
    email: str
    password: str
