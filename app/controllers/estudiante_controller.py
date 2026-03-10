import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.estudiante_model import Estudiante


class EstudianteController:

    def create_estudiante(self, estudiante: Estudiante):

        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO estudiante
                (id_facultad, id_programa, id_usuario, primer_nombre, primer_apellido,
                tipo_identificacion, numero_identificacion, genero, telefono, direccion, fecha_registro)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (
                    estudiante.id_facultad,
                    estudiante.id_programa,
                    estudiante.id_usuario,
                    estudiante.primer_nombre,
                    estudiante.primer_apellido,
                    estudiante.tipo_identificacion,
                    estudiante.numero_identificacion,
                    estudiante.genero,
                    estudiante.telefono,
                    estudiante.direccion,
                    estudiante.fecha_registro
                )
            )

            conn.commit()

            return {"resultado": "Estudiante creado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            # Manejo de UNIQUE
            if "duplicate key value" in str(err):
                raise HTTPException(
                    status_code=400,
                    detail="El número de identificación ya está registrado"
                )

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_estudiante(self, numero_identificacion: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM estudiante WHERE numero_identificacion = %s",
                (numero_identificacion,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            content = {
                "id_estudiante": result[0],
                "id_facultad": result[1],
                "id_programa": result[2],
                "id_usuario": result[3],
                "primer_nombre": result[4],
                "primer_apellido": result[5],
                "tipo_identificacion": result[6],
                "numero_identificacion": result[7],
                "genero": result[8],
                "telefono": result[9],
                "direccion": result[10],
                "fecha_registro": result[11]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_estudiantes(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM estudiante")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiantes no encontrados")

            payload = []

            for data in result:

                payload.append({
                    "id_estudiante": data[0],
                    "id_facultad": data[1],
                    "id_programa": data[2],
                    "id_usuario": data[3],
                    "primer_nombre": data[4],
                    "primer_apellido": data[5],
                    "tipo_identificacion": data[6],
                    "numero_identificacion": data[7],
                    "genero": data[8],
                    "telefono": data[9],
                    "direccion": data[10],
                    "fecha_registro": data[11]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_estudiante(self, id_estudiante: int, estudiante: Estudiante):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE estudiante SET
                id_facultad = %s,
                id_programa = %s,
                id_usuario = %s,
                primer_nombre = %s,
                primer_apellido = %s,
                tipo_identificacion = %s,
                numero_identificacion = %s,
                genero = %s,
                telefono = %s,
                direccion = %s,
                fecha_registro = %s
                WHERE id_estudiante = %s""",
                (
                    estudiante.id_facultad,
                    estudiante.id_programa,
                    estudiante.id_usuario,
                    estudiante.primer_nombre,
                    estudiante.primer_apellido,
                    estudiante.tipo_identificacion,
                    estudiante.numero_identificacion,
                    estudiante.genero,
                    estudiante.telefono,
                    estudiante.direccion,
                    estudiante.fecha_registro,
                    id_estudiante
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            conn.commit()

            return {"resultado": "Estudiante actualizado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            if "duplicate key value" in str(err):
                raise HTTPException(
                    status_code=400,
                    detail="El número de identificación ya está registrado"
                )

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_estudiante(self, id_estudiante: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM estudiante WHERE id_estudiante = %s",
                (id_estudiante,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            conn.commit()

            return {"resultado": f"Estudiante con id {id_estudiante} eliminado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


estudiante_controller = EstudianteController()

