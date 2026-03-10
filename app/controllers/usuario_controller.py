import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.usuario_model import Usuario


class UsuarioController:

    def create_usuario(self, usuario: Usuario):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """INSERT INTO usuario
                (primer_nombre,primer_apellido,telefono,email,password,estado,id_rol)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",

                (
                    usuario.primer_nombre,
                    usuario.primer_apellido,
                    usuario.telefono,
                    usuario.email,
                    usuario.password,
                    usuario.estado,
                    usuario.id_rol
                )
            )

            conn.commit()

            return {"resultado":"Usuario creado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_usuario(self,id_usuario:int):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                "SELECT * FROM usuario WHERE id_usuario=%s",
                (id_usuario,)
            )

            result=cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404,detail="Usuario no encontrado")

            content={
                "id_usuario":result[0],
                "primer_nombre":result[1],
                "primer_apellido":result[2],
                "telefono":result[3],
                "email":result[4],
                "password":result[5],
                "estado":result[6],
                "id_rol":result[7]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def get_usuarios(self):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute("SELECT * FROM usuario")

            result=cursor.fetchall()

            payload=[]

            for data in result:

                payload.append({
                    "id_usuario":data[0],
                    "primer_nombre":data[1],
                    "primer_apellido":data[2],
                    "telefono":data[3],
                    "email":data[4],
                    "password":data[5],
                    "estado":data[6],
                    "id_rol":data[7]
                })

            return {"resultado":jsonable_encoder(payload)}

        except psycopg2.Error as err:

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def update_usuario(self,id_usuario:int,usuario:Usuario):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                """UPDATE usuario SET
                primer_nombre=%s,
                primer_apellido=%s,
                telefono=%s,
                email=%s,
                password=%s,
                estado=%s,
                id_rol=%s
                WHERE id_usuario=%s""",

                (
                    usuario.primer_nombre,
                    usuario.primer_apellido,
                    usuario.telefono,
                    usuario.email,
                    usuario.password,
                    usuario.estado,
                    usuario.id_rol,
                    id_usuario
                )
            )

            conn.commit()

            return {"resultado":"Usuario actualizado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


    def delete_usuario(self,id_usuario:int):

        conn=None

        try:

            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                "DELETE FROM usuario WHERE id_usuario=%s",
                (id_usuario,)
            )

            conn.commit()

            return {"resultado":"Usuario eliminado"}

        except psycopg2.Error as err:

            if conn:
                conn.rollback()

            raise HTTPException(status_code=500,detail=str(err))

        finally:

            if conn:
                conn.close()


usuario_controller=UsuarioController()
