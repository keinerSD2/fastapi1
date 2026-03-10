import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.rol_model import Rol


class RolController:

    def create_rol(self, rol: Rol):

        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO rol
                (nombre, descripcion, acceso_privilegiado)
                VALUES (%s,%s,%s)""",
                (
                    rol.nombre,
                    rol.descripcion,
                    rol.acceso_privilegiado
                )
            )

            conn.commit()

            return {"resultado": "Rol creado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_rol(self, id_rol: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM rol WHERE id_rol = %s",
                (id_rol,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            content = {
                "id_rol": result[0],
                "nombre": result[1],
                "descripcion": result[2],
                "acceso_privilegiado": result[3]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_roles(self):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM rol")

            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="Roles no encontrados")

            payload = []

            for data in result:

                payload.append({
                    "id_rol": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "acceso_privilegiado": data[3]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_rol(self, id_rol: int, rol: Rol):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE rol SET
                nombre = %s,
                descripcion = %s,
                acceso_privilegiado = %s
                WHERE id_rol = %s""",
                (
                    rol.nombre,
                    rol.descripcion,
                    rol.acceso_privilegiado,
                    id_rol
                )
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            conn.commit()

            return {"resultado": "Rol actualizado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_rol(self, id_rol: int):

        conn = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM rol WHERE id_rol = %s",
                (id_rol,)
            )

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            conn.commit()

            return {"resultado": f"Rol con id {id_rol} eliminado correctamente"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500, detail=str(err))

        finally:

            if conn:
                conn.close()


rol_controller = RolController()
