from flask import Blueprint
from src.api.estados.controller import listar_estados, crear_estado, obtener_estado, actualizar_estado, eliminar_estado

estado_bp = Blueprint('estado_bp', __name__, url_prefix='/api/estados')

estado_bp.get('/')(listar_estados)
estado_bp.post('/')(crear_estado)
estado_bp.get('/<uuid:id>')(obtener_estado)
estado_bp.put('/<uuid:id>')(actualizar_estado)
estado_bp.delete('/<uuid:id>')(eliminar_estado)
