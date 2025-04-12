from database.database import get_connection
from ..models.entities.Miembros import Miembro


class MiembroModel:
    @classmethod
    def get_all_miembros(cls):
        try:
            connection = get_connection()
            miembro_list = []
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_miembro, nombre, apellido, direccion, telefono, email, fecha_registro
                    FROM miembros
                    ORDER BY nombre ASC
                    """
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    miembro = Miembro(
                        id_miembro=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        direccion=row[3],
                        telefono=row[4],
                        email=row[5],
                        fecha_registro=row[6],
                    )
                    miembro_list.append(miembro.to_JSON())
            connection.close()
            return miembro_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_miembro_by_id(cls, miembro_id):
        try:
            connection = get_connection()
            miembro_json = None
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_miembro, nombre, apellido, direccion, telefono, email, fecha_registro
                    FROM miembros
                    WHERE id_miembro = %s
                    """,
                    (miembro_id,),
                )
                row = cursor.fetchone()
                if row is not None:
                    miembro = Miembro(
                        id_miembro=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        direccion=row[3],
                        telefono=row[4],
                        email=row[5],
                        fecha_registro=row[6],
                    )
                    miembro_json = miembro.to_JSON()
                connection.close()
                return miembro_json
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_miembro(cls, miembro: Miembro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO miembros (id_miembro, nombre, apellido, direccion, telefono, email, fecha_registro)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        miembro.id_miembro,
                        miembro.nombre,
                        miembro.apellido,
                        miembro.direccion,
                        miembro.telefono,
                        miembro.email,
                        miembro.fecha_registro,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_miembro(cls, miembro: Miembro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE miembros
                    SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s, fecha_registro = %s
                    WHERE id_miembro = %s
                    """,
                    (
                        miembro.nombre,
                        miembro.apellido,
                        miembro.direccion,
                        miembro.telefono,
                        miembro.email,
                        miembro.fecha_registro,
                        miembro.id_miembro,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_miembro(cls, miembro: Miembro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM miembros
                    WHERE id_miembro = %s
                    """,
                    (miembro.id_miembro,),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
