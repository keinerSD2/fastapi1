import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.auth_model import Login, Register
from fastapi.encoders import jsonable_encoder

class AuthController:

    def login(self, datos: Login):
        email = datos.email
        password = datos.password

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()
            if result:
                return {"resultado": "Login exitoso"}
            else:
                raise HTTPException(status_code=401, detail="Credenciales inválidas")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def register(self, datos: Register):
        primer_nombre = datos.primer_nombre
        primer_apellido = datos.primer_apellido
        email = datos.email
        password = datos.password

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario FROM usuario WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                return {"error": "El usuario ya existe"}

            cursor.execute(
                "INSERT INTO usuario (primer_nombre,primer_apellido,email,password) VALUES (%s,%s,%s,%s)", (primer_nombre, primer_apellido, email, password))
            conn.commit()

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

        return {"resultado": "Registro exitoso"}
