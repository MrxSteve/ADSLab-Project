from flask import request, jsonify
from src.db.database import db
from src.db.models.multas import Multa
from src.db.models.prestamos import Prestamo
from src.db.models.miembros import Miembro
from flasgger import swag_from

# Twilio
from src.utils.whatsapp_notification import enviar_mensaje_whatsapp

@swag_from({
    'tags': ['Multas'],
    'description': 'Lista todas las multas registradas',
    'responses': {
        200: {
            'description': 'Listado de multas'
        }
    }
})
def listar_multas():
    multas = Multa.query.all()
    resultado = [{
        'id': str(m.id),
        'prestamo_id': str(m.prestamo_id),
        'monto': float(m.monto),
        'descripcion': m.descripcion,
        'pagada': m.pagada
    } for m in multas]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Multas'],
    'description': 'Crea una nueva multa',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'prestamo_id': 'uuid-prestamo',
                    'monto': 10.50,
                    'descripcion': 'Entrega tardía',
                    'pagada': False
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Multa creada correctamente'
        }
    }
})
def crear_multa():
    data = request.get_json()

    prestamo = Prestamo.query.get_or_404(data['prestamo_id'])
    miembro = Miembro.query.get_or_404(prestamo.miembro_id)

    nueva = Multa(
        prestamo_id=data['prestamo_id'],
        monto=data['monto'],
        descripcion=data.get('descripcion'),
        pagada=data.get('pagada', False)
    )
    db.session.add(nueva)
    db.session.commit()

    # Enviar notificación
    enviar_mensaje_whatsapp(
        mensaje=f'¡Hola! Tienes una multa de ${data["monto"]} pendiente. Por favor, realizar el pago lo antes posible.',
        numero_destino=miembro.telefono
    )

    return jsonify({'message': 'Multa creada correctamente'}), 201
    

@swag_from({
    'tags': ['Multas'],
    'description': 'Obtiene una multa por ID',
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
            'description': 'Datos de la multa'
        }
    }
})
def obtener_multa(id):
    multa = Multa.query.get_or_404(id)
    return jsonify({
        'id': str(multa.id),
        'prestamo_id': str(multa.prestamo_id),
        'monto': float(multa.monto),
        'descripcion': multa.descripcion,
        'pagada': multa.pagada
    }), 200


@swag_from({
    'tags': ['Multas'],
    'description': 'Actualiza una multa por ID',
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
                    'monto': 15.75,
                    'descripcion': 'Pago tardío',
                    'pagada': True
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Multa actualizada correctamente'
        }
    }
})
def actualizar_multa(id):
    multa = Multa.query.get_or_404(id)
    data = request.get_json()

    multa.monto = data['monto']
    multa.descripcion = data.get('descripcion')
    multa.pagada = data.get('pagada', multa.pagada)

    db.session.commit()
    return jsonify({'message': 'Multa actualizada correctamente'}), 200


@swag_from({
    'tags': ['Multas'],
    'description': 'Elimina una multa por ID',
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
            'description': 'Multa eliminada correctamente'
        }
    }
})
def eliminar_multa(id):
    multa = Multa.query.get_or_404(id)
    db.session.delete(multa)
    db.session.commit()
    return jsonify({'message': 'Multa eliminada correctamente'}), 200
