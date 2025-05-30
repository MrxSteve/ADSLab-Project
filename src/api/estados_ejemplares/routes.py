from flask import Blueprint
from src.api.estados_ejemplares.controller import listar_estados, crear_estado, obtener_estado, actualizar_estado, eliminar_estado

estado_ejemplar_bp = Blueprint('estado_ejemplar_bp', __name__, url_prefix='/api/estados-ejemplares')

estado_ejemplar_bp.get('/')(listar_estados)
estado_ejemplar_bp.post('/')(crear_estado)
estado_ejemplar_bp.get('/<uuid:id>')(obtener_estado)
estado_ejemplar_bp.put('/<uuid:id>')(actualizar_estado)
estado_ejemplar_bp.delete('/<uuid:id>')(eliminar_estado)
