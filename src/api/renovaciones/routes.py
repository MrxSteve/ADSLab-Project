from flask import Blueprint
from src.api.renovaciones.controller import listar_renovaciones, crear_renovacion, obtener_renovacion, actualizar_renovacion, eliminar_renovacion

renovacion_bp = Blueprint('renovacion_bp', __name__, url_prefix='/api/renovaciones')

renovacion_bp.get('/')(listar_renovaciones)
renovacion_bp.post('/')(crear_renovacion)
renovacion_bp.get('/<uuid:id>')(obtener_renovacion)
renovacion_bp.put('/<uuid:id>')(actualizar_renovacion)
renovacion_bp.delete('/<uuid:id>')(eliminar_renovacion)
