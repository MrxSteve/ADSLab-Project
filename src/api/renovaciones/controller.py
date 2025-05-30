from flask import request, jsonify
from src.db.database import db
from src.db.models.renovaciones import Renovacion
from src.db.models.prestamos import Prestamo
from flasgger import swag_from


@swag_from({
    'tags': ['Renovaciones'],
    'description': 'Lista todas las renovaciones registradas',
    'responses': {
        200: {
            'description': 'Listado de renovaciones'
        }
    }
})
def listar_renovaciones():
    renovaciones = Renovacion.query.all()
    resultado = [{
        'id': str(r.id),
        'prestamo_id': str(r.prestamo_id),
        'fecha_renovacion': r.fecha_renovacion.strftime('%Y-%m-%d')
    } for r in renovaciones]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Renovaciones'],
    'description': 'Crea una nueva renovación',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'prestamo_id': 'uuid-prestamo',
                    'fecha_renovacion': '2024-04-01'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Renovación registrada correctamente'
        }
    }
})
def crear_renovacion():
    data = request.get_json()

    Prestamo.query.get_or_404(data['prestamo_id'])

    nueva = Renovacion(
        prestamo_id=data['prestamo_id'],
        fecha_renovacion=data['fecha_renovacion']
    )
    db.session.add(nueva)
    db.session.commit()
    return jsonify({'message': 'Renovación registrada correctamente'}), 201


@swag_from({
    'tags': ['Renovaciones'],
    'description': 'Obtiene una renovación por ID',
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
            'description': 'Datos de la renovación'
        }
    }
})
def obtener_renovacion(id):
    renovacion = Renovacion.query.get_or_404(id)
    return jsonify({
        'id': str(renovacion.id),
        'prestamo_id': str(renovacion.prestamo_id),
        'fecha_renovacion': renovacion.fecha_renovacion.strftime('%Y-%m-%d')
    }), 200


@swag_from({
    'tags': ['Renovaciones'],
    'description': 'Actualiza una renovación por ID',
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
                    'fecha_renovacion': '2024-04-05'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Renovación actualizada correctamente'
        }
    }
})
def actualizar_renovacion(id):
    renovacion = Renovacion.query.get_or_404(id)
    data = request.get_json()

    renovacion.fecha_renovacion = data['fecha_renovacion']

    db.session.commit()
    return jsonify({'message': 'Renovación actualizada correctamente'}), 200


@swag_from({
    'tags': ['Renovaciones'],
    'description': 'Elimina una renovación por ID',
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
            'description': 'Renovación eliminada correctamente'
        }
    }
})
def eliminar_renovacion(id):
    renovacion = Renovacion.query.get_or_404(id)
    db.session.delete(renovacion)
    db.session.commit()
    return jsonify({'message': 'Renovación eliminada correctamente'}), 200
