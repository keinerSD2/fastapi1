import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.consulta_model import Consulta


class ConsultaController:

    def create_consulta(self, consulta: Consulta):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO consulta
                (id_estudiante, id_usuario, diagnostico, observaciones, motivo_consulta, fecha_entrada, fecha_salida)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",

                (
                    consulta.id_estudiante,
                    consulta.id_usuario,
                    consulta.diagnostico,
                    consulta.observaciones,
                    consulta.motivo_consulta,
                    consulta.fecha_entrada,
                    consulta.fecha_salida
                )
            )

            conn.commit()

            return {"resultado": "Consulta creada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_consulta(self, id_consulta: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM consulta WHERE id_consulta = %s",
                (id_consulta,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")

            content = {
                "id_consulta": result[0],
                "id_estudiante": result[1],
                "id_usuario": result[2],
                "diagnostico": result[3],
                "observaciones": result[4],
                "motivo_consulta": result[5],
                "fecha_entrada": result[6],
                "fecha_salida": result[7]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_consultas(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM consulta")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Consultas no encontradas")

            payload = []

            for data in result:

                payload.append({
                    "id_consulta": data[0],
                    "id_estudiante": data[1],
                    "id_usuario": data[2],
                    "diagnostico": data[3],
                    "observaciones": data[4],
                    "motivo_consulta": data[5],
                    "fecha_entrada": data[6],
                    "fecha_salida": data[7]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()

    def get_consultas_estudiante(self, id_estudiante: int):

        conn = None
    
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
    
            cursor.execute(
                "SELECT * FROM consulta WHERE id_estudiante = %s",
                (id_estudiante,)
            )
    
            result = cursor.fetchall()
    
            payload = []
    
            for data in result:
                payload.append({
                    "id_consulta": data[0],
                    "id_estudiante": data[1],
                    "id_usuario": data[2],
                    "diagnostico": data[3],
                    "observaciones": data[4],
                    "motivo_consulta": data[5],
                    "fecha_entrada": data[6],
                    "fecha_salida": data[7]
                })
    
            return {"resultado": jsonable_encoder(payload)}
    
        except psycopg2.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
    
        finally:
            if conn:
                conn.close()


    def update_consulta(self, id_consulta: int, consulta: Consulta):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE consulta SET
                id_estudiante = %s,
                id_usuario = %s,
                diagnostico = %s,
                observaciones = %s,
                motivo_consulta = %s,
                fecha_entrada = %s,
                fecha_salida = %s
                WHERE id_consulta = %s""",

                (
                    consulta.id_estudiante,
                    consulta.id_usuario,
                    consulta.diagnostico,
                    consulta.observaciones,
                    consulta.motivo_consulta,
                    consulta.fecha_entrada,
                    consulta.fecha_salida,
                    id_consulta
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")

            conn.commit()

            return {"resultado": "Consulta actualizada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_consulta(self, id_consulta: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM consulta WHERE id_consulta = %s",
                (id_consulta,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Consulta no encontrada")

            conn.commit()

            return {"resultado": f"Consulta con id {id_consulta} eliminada correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


consulta_controller = ConsultaController()


