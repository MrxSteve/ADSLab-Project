from flask import request, jsonify
from src.db.database import db
from src.db.models.estados import Estado
from flasgger import swag_from


@swag_from({
    'tags': ['Estados'],
    'description': 'Lista todos los estados',
    'responses': {
        200: {
            'description': 'Listado de estados'
        }
    }
})
def listar_estados():
    estados = Estado.query.all()
    resultado = [{'id': str(e.id), 'nombre': e.nombre} for e in estados]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Estados'],
    'description': 'Crea un nuevo estado',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'nombre': 'Activo'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Estado creado exitosamente'
        }
    }
})
def crear_estado():
    data = request.get_json()
    nuevo = Estado(nombre=data['nombre'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Estado creado exitosamente'}), 201


@swag_from({
    'tags': ['Estados'],
    'description': 'Obtiene un estado por ID',
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
            'description': 'Datos del estado'
        }
    }
})
def obtener_estado(id):
    estado = Estado.query.get_or_404(id)
    return jsonify({'id': str(estado.id), 'nombre': estado.nombre}), 200


@swag_from({
    'tags': ['Estados'],
    'description': 'Actualiza un estado por ID',
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
                    'nombre': 'Finalizado'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Estado actualizado correctamente'
        }
    }
})
def actualizar_estado(id):
    estado = Estado.query.get_or_404(id)
    data = request.get_json()
    estado.nombre = data['nombre']
    db.session.commit()
    return jsonify({'message': 'Estado actualizado correctamente'}), 200


@swag_from({
    'tags': ['Estados'],
    'description': 'Elimina un estado por ID',
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
            'description': 'Estado eliminado correctamente'
        }
    }
})
def eliminar_estado(id):
    estado = Estado.query.get_or_404(id)
    db.session.delete(estado)
    db.session.commit()
    return jsonify({'message': 'Estado eliminado correctamente'}), 200
