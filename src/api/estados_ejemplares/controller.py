from flask import request, jsonify
from src.db.database import db
from src.db.models.estados_ejemplares import EstadoEjemplar
from flasgger import swag_from


@swag_from({
    'tags': ['Estados Ejemplares'],
    'description': 'Lista todos los estados de ejemplares',
    'responses': {
        200: {
            'description': 'Listado de estados de ejemplares'
        }
    }
})
def listar_estados():
    estados = EstadoEjemplar.query.all()
    resultado = [{'id': str(e.id), 'nombre': e.nombre} for e in estados]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Estados Ejemplares'],
    'description': 'Crea un nuevo estado de ejemplar',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'nombre': 'Disponible'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Estado ejemplar creado exitosamente'
        }
    }
})
def crear_estado():
    data = request.get_json()
    nuevo = EstadoEjemplar(nombre=data['nombre'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Estado ejemplar creado exitosamente'}), 201


@swag_from({
    'tags': ['Estados Ejemplares'],
    'description': 'Obtiene un estado ejemplar por ID',
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
            'description': 'Datos del estado ejemplar'
        }
    }
})
def obtener_estado(id):
    estado = EstadoEjemplar.query.get_or_404(id)
    return jsonify({'id': str(estado.id), 'nombre': estado.nombre}), 200


@swag_from({
    'tags': ['Estados Ejemplares'],
    'description': 'Actualiza un estado ejemplar por ID',
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
                    'nombre': 'Dañado'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Estado ejemplar actualizado correctamente'
        }
    }
})
def actualizar_estado(id):
    estado = EstadoEjemplar.query.get_or_404(id)
    data = request.get_json()
    estado.nombre = data['nombre']
    db.session.commit()
    return jsonify({'message': 'Estado ejemplar actualizado correctamente'}), 200


@swag_from({
    'tags': ['Estados Ejemplares'],
    'description': 'Elimina un estado ejemplar por ID',
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
            'description': 'Estado ejemplar eliminado correctamente'
        }
    }
})
def eliminar_estado(id):
    estado = EstadoEjemplar.query.get_or_404(id)
    db.session.delete(estado)
    db.session.commit()
    return jsonify({'message': 'Estado ejemplar eliminado correctamente'}), 200
