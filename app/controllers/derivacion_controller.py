import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.derivacion_model import Derivacion


class DerivacionController:

    def create_derivacion(self, derivacion: Derivacion):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO derivacion
                (id_consulta, id_clinica, razon, fecha)
                VALUES (%s,%s,%s,%s)""",

                (
                    derivacion.id_consulta,
                    derivacion.id_clinica,
                    derivacion.razon,
                    derivacion.fecha
                )
            )

            conn.commit()

            return {"resultado": "Derivación creada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_derivacion(self, id_derivacion: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM derivacion WHERE id_derivacion = %s",
                (id_derivacion,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Derivación no encontrada")

            content = {
                "id_derivacion": result[0],
                "id_consulta": result[1],
                "id_clinica": result[2],
                "razon": result[3],
                "fecha": result[4]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_derivaciones(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM derivacion")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Derivaciones no encontradas")

            payload = []

            for data in result:

                payload.append({
                    "id_derivacion": data[0],
                    "id_consulta": data[1],
                    "id_clinica": data[2],
                    "razon": data[3],
                    "fecha": data[4]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_derivacion(self, id_derivacion: int, derivacion: Derivacion):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE derivacion SET
                id_consulta = %s,
                id_clinica = %s,
                razon = %s,
                fecha = %s
                WHERE id_derivacion = %s""",

                (
                    derivacion.id_consulta,
                    derivacion.id_clinica,
                    derivacion.razon,
                    derivacion.fecha,
                    id_derivacion
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Derivación no encontrada")

            conn.commit()

            return {"resultado": "Derivación actualizada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_derivacion(self, id_derivacion: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM derivacion WHERE id_derivacion = %s",
                (id_derivacion,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Derivación no encontrada")

            conn.commit()

            return {"resultado": f"Derivación con id {id_derivacion} eliminada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


derivacion_controller = DerivacionController()
