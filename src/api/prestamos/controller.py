from flask import request, jsonify
from src.db.database import db
from src.db.models.prestamos import Prestamo
from src.db.models.miembros import Miembro
from src.db.models.ejemplares import Ejemplar
from src.db.models.estados import Estado
from flasgger import swag_from

# Twilio
from src.utils.whatsapp_notification import enviar_mensaje_whatsapp

@swag_from({
    'tags': ['Préstamos'],
    'description': 'Lista todos los préstamos registrados',
    'responses': {
        200: {
            'description': 'Listado de préstamos'
        }
    }
})
def listar_prestamos():
    prestamos = Prestamo.query.all()
    resultado = [{
        'id': str(p.id),
        'miembro_id': str(p.miembro_id),
        'ejemplar_id': str(p.ejemplar_id),
        'estado_id': str(p.estado_id)
    } for p in prestamos]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Préstamos'],
    'description': 'Crea un nuevo préstamo',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'miembro_id': 'uuid-miembro',
                    'ejemplar_id': 'uuid-ejemplar',
                    'estado_id': 'uuid-estado'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Préstamo creado exitosamente'
        }
    }
})
def crear_prestamo():
    data = request.get_json()

    miembro = Miembro.query.get_or_404(data['miembro_id'])
    Ejemplar.query.get_or_404(data['ejemplar_id'])
    Estado.query.get_or_404(data['estado_id'])

    nuevo = Prestamo(
        miembro_id=miembro.id,
        ejemplar_id=data['ejemplar_id'],
        estado_id=data['estado_id']
    )
    db.session.add(nuevo)
    db.session.commit()
    
    # Enviar notificacion
    enviar_mensaje_whatsapp(
        mensaje='Hola, tu préstamo fue registrado correctamente. ¡Gracias por preferirnos!',
        numero_destino=miembro.telefono
    )

    return jsonify({'message': 'Préstamo creado exitosamente'}), 201

@swag_from({
    'tags': ['Préstamos'],
    'description': 'Obtiene un préstamo por ID',
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
            'description': 'Datos del préstamo'
        }
    }
})
def obtener_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    return jsonify({
        'id': str(prestamo.id),
        'miembro_id': str(prestamo.miembro_id),
        'ejemplar_id': str(prestamo.ejemplar_id),
        'estado_id': str(prestamo.estado_id)
    }), 200


@swag_from({
    'tags': ['Préstamos'],
    'description': 'Actualiza un préstamo por ID',
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
                    'miembro_id': 'uuid-miembro',
                    'ejemplar_id': 'uuid-ejemplar',
                    'estado_id': 'uuid-estado'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Préstamo actualizado correctamente'
        }
    }
})
def actualizar_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    data = request.get_json()

    if 'miembro_id' in data:
        Miembro.query.get_or_404(data['miembro_id'])
        prestamo.miembro_id = data['miembro_id']

    if 'ejemplar_id' in data:
        Ejemplar.query.get_or_404(data['ejemplar_id'])
        prestamo.ejemplar_id = data['ejemplar_id']

    if 'estado_id' in data:
        Estado.query.get_or_404(data['estado_id'])
        prestamo.estado_id = data['estado_id']

    db.session.commit()
    return jsonify({'message': 'Préstamo actualizado correctamente'}), 200


@swag_from({
    'tags': ['Préstamos'],
    'description': 'Elimina un préstamo por ID',
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
            'description': 'Préstamo eliminado correctamente'
        }
    }
})
def eliminar_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    db.session.delete(prestamo)
    db.session.commit()
    return jsonify({'message': 'Préstamo eliminado correctamente'}), 200
