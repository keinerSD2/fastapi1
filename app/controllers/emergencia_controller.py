import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.emergencia_model import Emergencia


class EmergenciaController:

    def create_emergencia(self, emergencia: Emergencia):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO emergencia
                (id_usuario, id_estudiante, fecha, descripcion, atencion_prestada)
                VALUES (%s,%s,%s,%s,%s)""",

                (
                    emergencia.id_usuario,
                    emergencia.id_estudiante,
                    emergencia.fecha,
                    emergencia.descripcion,
                    emergencia.atencion_prestada
                )
            )

            conn.commit()

            return {"resultado": "Emergencia registrada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_emergencia(self, id_emergencia: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM emergencia WHERE id_emergencia = %s",
                (id_emergencia,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Emergencia no encontrada")

            content = {
                "id_emergencia": result[0],
                "id_usuario": result[1],
                "id_estudiante": result[2],
                "fecha": result[3],
                "descripcion": result[4],
                "atencion_prestada": result[5]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_emergencias(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM emergencia")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Emergencias no encontradas")

            payload = []

            for data in result:

                payload.append({
                    "id_emergencia": data[0],
                    "id_usuario": data[1],
                    "id_estudiante": data[2],
                    "fecha": data[3],
                    "descripcion": data[4],
                    "atencion_prestada": data[5]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_emergencia(self, id_emergencia: int, emergencia: Emergencia):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE emergencia SET
                id_usuario = %s,
                id_estudiante = %s,
                fecha = %s,
                descripcion = %s,
                atencion_prestada = %s
                WHERE id_emergencia = %s""",

                (
                    emergencia.id_usuario,
                    emergencia.id_estudiante,
                    emergencia.fecha,
                    emergencia.descripcion,
                    emergencia.atencion_prestada,
                    id_emergencia
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Emergencia no encontrada")

            conn.commit()

            return {"resultado": "Emergencia actualizada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_emergencia(self, id_emergencia: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM emergencia WHERE id_emergencia = %s",
                (id_emergencia,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Emergencia no encontrada")

            conn.commit()

            return {"resultado": f"Emergencia con id {id_emergencia} eliminada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


emergencia_controller = EmergenciaController()
