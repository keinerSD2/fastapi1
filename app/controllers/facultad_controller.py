import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.facultad_model import Facultad


class FacultadController:

    def create_facultad(self, facultad: Facultad):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """INSERT INTO facultad (nombre,descripcion)
                VALUES (%s,%s)""",

                (
                    facultad.nombre,
                    facultad.descripcion
                )
            )

            conn.commit()

            return {"resultado":"Facultad creada"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_facultad(self,id_facultad:int):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                "SELECT * FROM facultad WHERE id_facultad=%s",
                (id_facultad,)
            )

            result=cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404,detail="Facultad no encontrada")

            content={
                "id_facultad":result[0],
                "nombre":result[1],
                "descripcion":result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_facultades(self):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute("SELECT * FROM facultad")

            result=cursor.fetchall()

            payload=[]

            for data in result:

                payload.append({
                    "id_facultad":data[0],
                    "nombre":data[1],
                    "descripcion":data[2]
                })

            return {"resultado":jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_facultad(self,id_facultad:int,facultad:Facultad):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """UPDATE facultad SET
                nombre=%s,
                descripcion=%s
                WHERE id_facultad=%s""",

                (
                    facultad.nombre,
                    facultad.descripcion,
                    id_facultad
                )
            )

            conn.commit()

            return {"resultado":"Facultad actualizada"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_facultad(self,id_facultad:int):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                "DELETE FROM facultad WHERE id_facultad=%s",
                (id_facultad,)
            )

            conn.commit()

            return {"resultado":"Facultad eliminada"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


facultad_controller=FacultadController()
