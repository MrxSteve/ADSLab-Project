from database.database import get_connection
from ..models.entities.Libros import Libro


class LibroModel:

    @classmethod
    def get_all_libros(cls):
        try:
            connection = get_connection()
            libros_list = []
            with connection.cursor() as cursor:

                cursor.execute(
                    """
                            SELECT id_libro, titulo, autor, editorial, anio_publicacion, genero
                    FROM libros
                    ORDER BY 
                    titulo ASC
                """
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    libro = Libro(
                        id_libro=row[0],
                        titulo=row[1],
                        autor=row[2],
                        editorial=row[3],
                        anio_publicacion=row[4],
                        genero=row[5],
                    )
                    libros_list.append(libro.to_JSON())
            connection.close()
            return libros_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_libro_by_id(cls, libro_id):
        try:
            connection = get_connection()
            libro_json = None
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                            SELECT id_libro, titulo, autor, editorial, anio_publicacion, genero
                    FROM libros
                    WHERE id_libro = %s
                """,
                    (libro_id,),
                )
                row = cursor.fetchone()
                if row is not None:
                    libro = Libro(
                        id_libro=row[0],
                        titulo=row[1],
                        autor=row[2],
                        editorial=row[3],
                        anio_publicacion=row[4],
                        genero=row[5],
                    )
                    libros_json = libro.to_JSON()
            connection.close()
            return libros_json
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_libro(cls, libro: Libro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO libros (id_libro, titulo, autor, editorial, anio_publicacion, genero)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        libro.id_libro,
                        libro.titulo,
                        libro.autor,
                        libro.editorial,
                        libro.anio_publicacion,
                        libro.genero,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_libro(cls, libro: Libro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                        UPDATE libros
                        SET titulo = %s, autor = %s, editorial = %s, anio_publicacion = %s, genero = %s
                        WHERE id_libro = %s
                    """,
                    (
                        libro.titulo,
                        libro.autor,
                        libro.editorial,
                        libro.anio_publicacion,
                        libro.genero,
                        libro.id_libro,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_libro(cls, libro: Libro):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                        DELETE FROM libros
                        WHERE id_libro = %s
                    """,
                    (libro.id_libro,),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
