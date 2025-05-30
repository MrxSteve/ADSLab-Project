from flask import request, jsonify
from src.db.database import db
from src.db.models.libros import Libro
from flasgger import swag_from


@swag_from({
    'tags': ['Libros'],
    'description': 'Lista todos los libros registrados',
    'responses': {
        200: {
            'description': 'Listado de libros'
        }
    }
})
def listar_libros():
    libros = Libro.query.all()
    resultado = [{
        'id': str(l.id),
        'titulo': l.titulo,
        'autor': l.autor,
        'editorial': l.editorial,
        'genero': l.genero
    } for l in libros]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Libros'],
    'description': 'Crea un nuevo libro',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'titulo': 'Cien años de soledad',
                    'autor': 'Gabriel García Márquez',
                    'editorial': 'Sudamericana',
                    'genero': 'Realismo mágico'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Libro creado exitosamente'
        }
    }
})
def crear_libro():
    data = request.get_json()
    nuevo = Libro(
        titulo=data['titulo'],
        autor=data.get('autor'),
        editorial=data.get('editorial'),
        genero=data.get('genero')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Libro creado exitosamente'}), 201


@swag_from({
    'tags': ['Libros'],
    'description': 'Obtiene un libro por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'string'
        }
    ],
    'responses': {
        200: {
            'description': 'Datos del libro'
        }
    }
})
def obtener_libro(id):
    libro = Libro.query.get_or_404(id)
    return jsonify({
        'id': str(libro.id),
        'titulo': libro.titulo,
        'autor': libro.autor,
        'editorial': libro.editorial,
        'genero': libro.genero
    }), 200


@swag_from({
    'tags': ['Libros'],
    'description': 'Actualiza un libro por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'string'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'titulo': 'El amor en los tiempos del cólera',
                    'autor': 'Gabriel García Márquez',
                    'editorial': 'Sudamericana',
                    'genero': 'Romance'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Libro actualizado correctamente'
        }
    }
})
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()
    libro.titulo = data['titulo']
    libro.autor = data.get('autor')
    libro.editorial = data.get('editorial')
    libro.genero = data.get('genero')
    db.session.commit()
    return jsonify({'message': 'Libro actualizado correctamente'}), 200


@swag_from({
    'tags': ['Libros'],
    'description': 'Elimina un libro por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'string'
        }
    ],
    'responses': {
        200: {
            'description': 'Libro eliminado correctamente'
        }
    }
})
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'message': 'Libro eliminado correctamente'}), 200
