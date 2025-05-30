from flask import request, jsonify
from src.db.database import db
from src.db.models.historial import Historial
from src.db.models.prestamos import Prestamo
from flasgger import swag_from


@swag_from({
    'tags': ['Historial'],
    'description': 'Lista todos los registros del historial',
    'responses': {
        200: {
            'description': 'Listado de historial'
        }
    }
})
def listar_historial():
    historial = Historial.query.all()
    resultado = [{
        'id': str(h.id),
        'prestamo_id': str(h.prestamo_id),
        'descripcion': h.descripcion,
        'fecha_registro': h.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
    } for h in historial]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Historial'],
    'description': 'Registra un nuevo historial',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'prestamo_id': 'uuid-prestamo',
                    'descripcion': 'Préstamo renovado'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Historial registrado correctamente'
        }
    }
})
def crear_historial():
    data = request.get_json()
    Prestamo.query.get_or_404(data['prestamo_id'])

    nuevo = Historial(
        prestamo_id=data['prestamo_id'],
        descripcion=data['descripcion']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'message': 'Historial registrado correctamente'}), 201


@swag_from({
    'tags': ['Historial'],
    'description': 'Obtiene un historial por ID',
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
            'description': 'Datos del historial'
        }
    }
})
def obtener_historial(id):
    historial = Historial.query.get_or_404(id)
    return jsonify({
        'id': str(historial.id),
        'prestamo_id': str(historial.prestamo_id),
        'descripcion': historial.descripcion,
        'fecha_registro': historial.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
    }), 200


@swag_from({
    'tags': ['Historial'],
    'description': 'Actualiza un historial por ID',
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
                    'descripcion': 'Ejemplar devuelto correctamente'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Historial actualizado correctamente'
        }
    }
})
def actualizar_historial(id):
    historial = Historial.query.get_or_404(id)
    data = request.get_json()
    historial.descripcion = data['descripcion']
    db.session.commit()
    return jsonify({'message': 'Historial actualizado correctamente'}), 200


@swag_from({
    'tags': ['Historial'],
    'description': 'Elimina un historial por ID',
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
            'description': 'Historial eliminado correctamente'
        }
    }
})
def eliminar_historial(id):
    historial = Historial.query.get_or_404(id)
    db.session.delete(historial)
    db.session.commit()
    return jsonify({'message': 'Historial eliminado correctamente'}), 200
