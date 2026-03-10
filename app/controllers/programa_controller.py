import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.programa_model import Programa


class ProgramaController:

    def create_programa(self,programa:Programa):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """INSERT INTO programa
                (id_facultad,nombre,descripcion)
                VALUES (%s,%s,%s)""",

                (
                    programa.id_facultad,
                    programa.nombre,
                    programa.descripcion
                )
            )

            conn.commit()

            return {"resultado":"Programa creado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()

    def get_programas_por_facultad(self, id_facultad: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id_programa, nombre FROM programa WHERE id_facultad = %s",
                (id_facultad,)
            )

            result = cursor.fetchall()

            if not result:
                return {"resultado": []}  # No hay programas para esa facultad

            payload = []
            for data in result:
                payload.append({
                    "id_programa": data[0],
                    "nombre": data[1]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn:
                conn.close()


    def get_programas(self):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute("SELECT * FROM programa")

            result=cursor.fetchall()

            payload=[]

            for data in result:

                payload.append({
                    "id_programa":data[0],
                    "id_facultad":data[1],
                    "nombre":data[2],
                    "descripcion":data[3]
                })

            return {"resultado":jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_programa(self,id_programa:int,programa:Programa):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """UPDATE programa SET
                id_facultad=%s,
                nombre=%s,
                descripcion=%s
                WHERE id_programa=%s""",

                (
                    programa.id_facultad,
                    programa.nombre,
                    programa.descripcion,
                    id_programa
                )
            )

            conn.commit()

            return {"resultado":"Programa actualizado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_programa(self,id_programa:int):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                "DELETE FROM programa WHERE id_programa=%s",
                (id_programa,)
            )

            conn.commit()

            return {"resultado":"Programa eliminado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


programa_controller=ProgramaController()


