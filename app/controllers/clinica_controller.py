import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.clinica_model import Clinica


class ClinicaController:

    def create_clinica(self, clinica: Clinica):

        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO clinica
                (nombre, ubicacion)
                VALUES (%s,%s)""",
                (
                    clinica.nombre,
                    clinica.ubicacion
                )
            )

            conn.commit()

            return {"resultado": "Clínica creada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_clinica(self, id_clinica: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM clinica WHERE id_clinica = %s",
                (id_clinica,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Clínica no encontrada")

            content = {
                "id_clinica": result[0],
                "nombre": result[1],
                "ubicacion": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_clinicas(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM clinica")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Clínicas no encontradas")

            payload = []

            for data in result:

                payload.append({
                    "id_clinica": data[0],
                    "nombre": data[1],
                    "ubicacion": data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_clinica(self, id_clinica: int, clinica: Clinica):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE clinica SET
                nombre = %s,
                ubicacion = %s
                WHERE id_clinica = %s""",
                (
                    clinica.nombre,
                    clinica.ubicacion,
                    id_clinica
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Clínica no encontrada")

            conn.commit()

            return {"resultado": "Clínica actualizada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_clinica(self, id_clinica: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM clinica WHERE id_clinica = %s",
                (id_clinica,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Clínica no encontrada")

            conn.commit()

            return {"resultado": f"Clínica con id {id_clinica} eliminada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


clinica_controller = ClinicaController()

