from flask import request, jsonify
from src.db.database import db
from src.db.models.ejemplares import Ejemplar
from src.db.models.libros import Libro
from src.db.models.estados_ejemplares import EstadoEjemplar
from flasgger import swag_from


@swag_from({
    'tags': ['Ejemplares'],
    'description': 'Lista todos los ejemplares',
    'responses': {
        200: {
            'description': 'Listado de ejemplares'
        }
    }
})
def listar_ejemplares():
    ejemplares = Ejemplar.query.all()
    resultado = [{
        'id': str(e.id),
        'codigo_interno': e.codigo_interno,
        'libro_id': str(e.libro_id),
        'estado_id': str(e.estado_id)
    } for e in ejemplares]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Ejemplares'],
    'description': 'Crea un nuevo ejemplar',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'codigo_interno': 'EJ-001',
                    'libro_id': 'uuid-libro',
                    'estado_id': 'uuid-estado'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Ejemplar creado exitosamente'
        }
    }
})
def crear_ejemplar():
    data = request.get_json()
    libro = Libro.query.get_or_404(data['libro_id'])
    estado = EstadoEjemplar.query.get_or_404(data['estado_id'])

    nuevo = Ejemplar(
        codigo_interno=data['codigo_interno'],
        libro_id=libro.id,
        estado_id=estado.id
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Ejemplar creado exitosamente'}), 201


@swag_from({
    'tags': ['Ejemplares'],
    'description': 'Obtiene un ejemplar por ID',
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
            'description': 'Datos del ejemplar'
        }
    }
})
def obtener_ejemplar(id):
    ejemplar = Ejemplar.query.get_or_404(id)
    return jsonify({
        'id': str(ejemplar.id),
        'codigo_interno': ejemplar.codigo_interno,
        'libro_id': str(ejemplar.libro_id),
        'estado_id': str(ejemplar.estado_id)
    }), 200


@swag_from({
    'tags': ['Ejemplares'],
    'description': 'Actualiza un ejemplar por ID',
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
                    'codigo_interno': 'EJ-002',
                    'libro_id': 'uuid-libro',
                    'estado_id': 'uuid-estado'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Ejemplar actualizado correctamente'
        }
    }
})
def actualizar_ejemplar(id):
    ejemplar = Ejemplar.query.get_or_404(id)
    data = request.get_json()

    if 'libro_id' in data:
        libro = Libro.query.get_or_404(data['libro_id'])
        ejemplar.libro_id = libro.id

    if 'estado_id' in data:
        estado = EstadoEjemplar.query.get_or_404(data['estado_id'])
        ejemplar.estado_id = estado.id

    ejemplar.codigo_interno = data['codigo_interno']
    db.session.commit()
    return jsonify({'message': 'Ejemplar actualizado correctamente'}), 200


@swag_from({
    'tags': ['Ejemplares'],
    'description': 'Elimina un ejemplar por ID',
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
            'description': 'Ejemplar eliminado correctamente'
        }
    }
})
def eliminar_ejemplar(id):
    ejemplar = Ejemplar.query.get_or_404(id)
    db.session.delete(ejemplar)
    db.session.commit()
    return jsonify({'message': 'Ejemplar eliminado correctamente'}), 200
