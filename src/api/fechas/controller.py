from flask import request, jsonify
from src.db.database import db
from src.db.models.fechas import Fecha
from src.db.models.prestamos import Prestamo
from flasgger import swag_from


@swag_from({
    'tags': ['Fechas'],
    'description': 'Lista todas las fechas registradas',
    'responses': {
        200: {
            'description': 'Listado de fechas'
        }
    }
})
def listar_fechas():
    fechas = Fecha.query.all()
    resultado = [{
        'id': str(f.id),
        'prestamo_id': str(f.prestamo_id),
        'fecha_inicio': f.fecha_inicio.strftime('%Y-%m-%d'),
        'fecha_fin': f.fecha_fin.strftime('%Y-%m-%d'),
        'fecha_devolucion': f.fecha_devolucion.strftime('%Y-%m-%d') if f.fecha_devolucion else None
    } for f in fechas]
    return jsonify(resultado), 200


@swag_from({
    'tags': ['Fechas'],
    'description': 'Registra una nueva fecha',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'example': {
                    'prestamo_id': 'uuid-prestamo',
                    'fecha_inicio': '2024-01-01',
                    'fecha_fin': '2024-01-15',
                    'fecha_devolucion': '2024-01-14'
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Fecha registrada correctamente'
        }
    }
})
def crear_fecha():
    data = request.get_json()
    Prestamo.query.get_or_404(data['prestamo_id'])

    nueva = Fecha(
        prestamo_id=data['prestamo_id'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin'],
        fecha_devolucion=data.get('fecha_devolucion')
    )
    db.session.add(nueva)
    db.session.commit()
    return jsonify({'message': 'Fecha registrada correctamente'}), 201


@swag_from({
    'tags': ['Fechas'],
    'description': 'Obtiene una fecha por ID',
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
            'description': 'Datos de la fecha'
        }
    }
})
def obtener_fecha(id):
    fecha = Fecha.query.get_or_404(id)
    return jsonify({
        'id': str(fecha.id),
        'prestamo_id': str(fecha.prestamo_id),
        'fecha_inicio': fecha.fecha_inicio.strftime('%Y-%m-%d'),
        'fecha_fin': fecha.fecha_fin.strftime('%Y-%m-%d'),
        'fecha_devolucion': fecha.fecha_devolucion.strftime('%Y-%m-%d') if fecha.fecha_devolucion else None
    }), 200


@swag_from({
    'tags': ['Fechas'],
    'description': 'Actualiza una fecha por ID',
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
                    'fecha_inicio': '2024-01-01',
                    'fecha_fin': '2024-01-15',
                    'fecha_devolucion': '2024-01-14'
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Fecha actualizada correctamente'
        }
    }
})
def actualizar_fecha(id):
    fecha = Fecha.query.get_or_404(id)
    data = request.get_json()

    fecha.fecha_inicio = data['fecha_inicio']
    fecha.fecha_fin = data['fecha_fin']
    fecha.fecha_devolucion = data.get('fecha_devolucion')

    db.session.commit()
    return jsonify({'message': 'Fecha actualizada correctamente'}), 200


@swag_from({
    'tags': ['Fechas'],
    'description': 'Elimina una fecha por ID',
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
            'description': 'Fecha eliminada correctamente'
        }
    }
})
def eliminar_fecha(id):
    fecha = Fecha.query.get_or_404(id)
    db.session.delete(fecha)
    db.session.commit()
    return jsonify({'message': 'Fecha eliminada correctamente'}), 200
