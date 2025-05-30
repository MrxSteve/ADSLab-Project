from flask import Blueprint
from src.api.ejemplares.controller import listar_ejemplares, crear_ejemplar, obtener_ejemplar, actualizar_ejemplar, eliminar_ejemplar

ejemplar_bp = Blueprint('ejemplar_bp', __name__, url_prefix='/api/ejemplares')

ejemplar_bp.get('/')(listar_ejemplares)
ejemplar_bp.post('/')(crear_ejemplar)
ejemplar_bp.get('/<uuid:id>')(obtener_ejemplar)
ejemplar_bp.put('/<uuid:id>')(actualizar_ejemplar)
ejemplar_bp.delete('/<uuid:id>')(eliminar_ejemplar)
