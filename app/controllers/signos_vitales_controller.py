import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.signos_vitales_model import SignosVitales


class SignosVitalesController:

    def create_signos(self, signos: SignosVitales):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO signos_vitales
                (id_consulta, presion_arterial, temperatura, peso, altura, saturacion_oxigeno, frecuencia_cardiaca, tipo_sangre)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",

                (
                    signos.id_consulta,
                    signos.presion_arterial,
                    signos.temperatura,
                    signos.peso,
                    signos.altura,
                    signos.saturacion_oxigeno,
                    signos.frecuencia_cardiaca,
                    signos.tipo_sangre
                )
            )

            conn.commit()

            return {"resultado": "Signos vitales registrados correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_signos(self, id_signos: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM signos_vitales WHERE id_signos = %s",
                (id_signos,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Signos vitales no encontrados")

            content = {
                "id_signos": result[0],
                "id_consulta": result[1],
                "presion_arterial": result[2],
                "temperatura": result[3],
                "peso": result[4],
                "altura": result[5],
                "saturacion_oxigeno": result[6],
                "frecuencia_cardiaca": result[7],
                "tipo_sangre": result[8]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_signos_all(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM signos_vitales")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay signos vitales registrados")

            payload = []

            for data in result:

                payload.append({
                    "id_signos": data[0],
                    "id_consulta": data[1],
                    "presion_arterial": data[2],
                    "temperatura": data[3],
                    "peso": data[4],
                    "altura": data[5],
                    "saturacion_oxigeno": data[6],
                    "frecuencia_cardiaca": data[7],
                    "tipo_sangre": data[8]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_signos(self, id_signos: int, signos: SignosVitales):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE signos_vitales SET
                id_consulta = %s,
                presion_arterial = %s,
                temperatura = %s,
                peso = %s,
                altura = %s,
                saturacion_oxigeno = %s,
                frecuencia_cardiaca = %s,
                tipo_sangre = %s
                WHERE id_signos = %s""",

                (
                    signos.id_consulta,
                    signos.presion_arterial,
                    signos.temperatura,
                    signos.peso,
                    signos.altura,
                    signos.saturacion_oxigeno,
                    signos.frecuencia_cardiaca,
                    signos.tipo_sangre,
                    id_signos
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Signos vitales no encontrados")

            conn.commit()

            return {"resultado": "Signos vitales actualizados correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_signos(self, id_signos: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM signos_vitales WHERE id_signos = %s",
                (id_signos,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Signos vitales no encontrados")

            conn.commit()

            return {"resultado": f"Signos vitales con id {id_signos} eliminados correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


signos_vitales_controller = SignosVitalesController()
