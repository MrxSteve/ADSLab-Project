from flask import Blueprint
from src.api.fechas.controller import listar_fechas, crear_fecha, obtener_fecha, actualizar_fecha, eliminar_fecha

fecha_bp = Blueprint('fecha_bp', __name__, url_prefix='/api/fechas')

fecha_bp.get('/')(listar_fechas)
fecha_bp.post('/')(crear_fecha)
fecha_bp.get('/<uuid:id>')(obtener_fecha)
fecha_bp.put('/<uuid:id>')(actualizar_fecha)
fecha_bp.delete('/<uuid:id>')(eliminar_fecha)
