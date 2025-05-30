from flask import request, jsonify
from src.db.database import db
from src.db.models.miembros import Miembro
from flasgger import swag_from


@swag_from({
    'tags': ['Miembros'],
    'description': 'Lista todos los miembros registrados',
    'responses': {
        200: {
            'description': 'Listado de miembros'
        }
    }
})
def listar_miembros():
    miembros = Miembro.query.all()
    resultado = [{
        'id': str(m.id),
        'nombre': m.nombre,
        'apellido': m.apellido,
        'direccion': m.direccion,
        'telefono': m.telefono,
        'email': m.email
    } for m in miembros]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Miembros'],
    'description': 'Crea un nuevo miembro',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'nombre': 'Juan',
                    'apellido': 'Perez',
                    'direccion': 'San Salvador',
                    'telefono': '7777-8888',
                    'email': 'juan@gmail.com'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Miembro creado exitosamente'
        }
    }
})
def crear_miembro():
    data = request.get_json()
    nuevo = Miembro(
        nombre=data['nombre'],
        apellido=data['apellido'],
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        email=data.get('email')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Miembro creado exitosamente'}), 201


@swag_from({
    'tags': ['Miembros'],
    'description': 'Obtiene un miembro por ID',
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
            'description': 'Datos del miembro'
        }
    }
})
def obtener_miembro(id):
    miembro = Miembro.query.get_or_404(id)
    return jsonify({
        'id': str(miembro.id),
        'nombre': miembro.nombre,
        'apellido': miembro.apellido,
        'direccion': miembro.direccion,
        'telefono': miembro.telefono,
        'email': miembro.email
    }), 200


@swag_from({
    'tags': ['Miembros'],
    'description': 'Actualiza un miembro por ID',
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
                    'nombre': 'Carlos',
                    'apellido': 'Mendez',
                    'direccion': 'Santa Ana',
                    'telefono': '7777-0000',
                    'email': 'carlos@gmail.com'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Miembro actualizado correctamente'
        }
    }
})
def actualizar_miembro(id):
    miembro = Miembro.query.get_or_404(id)
    data = request.get_json()
    miembro.nombre = data['nombre']
    miembro.apellido = data['apellido']
    miembro.direccion = data.get('direccion')
    miembro.telefono = data.get('telefono')
    miembro.email = data.get('email')
    db.session.commit()
    return jsonify({'message': 'Miembro actualizado correctamente'}), 200


@swag_from({
    'tags': ['Miembros'],
    'description': 'Elimina un miembro por ID',
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
            'description': 'Miembro eliminado correctamente'
        }
    }
})
def eliminar_miembro(id):
    miembro = Miembro.query.get_or_404(id)
    db.session.delete(miembro)
    db.session.commit()
    return jsonify({'message': 'Miembro eliminado correctamente'}), 200
