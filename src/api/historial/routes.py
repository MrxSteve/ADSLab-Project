from flask import Blueprint
from src.api.historial.controller import listar_historial, crear_historial, obtener_historial, actualizar_historial, eliminar_historial

historial_bp = Blueprint('historial_bp', __name__, url_prefix='/api/historial')

historial_bp.get('/')(listar_historial)
historial_bp.post('/')(crear_historial)
historial_bp.get('/<uuid:id>')(obtener_historial)
historial_bp.put('/<uuid:id>')(actualizar_historial)
historial_bp.delete('/<uuid:id>')(eliminar_historial)
