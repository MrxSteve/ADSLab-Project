from flask import Blueprint
from src.api.miembros.controller import listar_miembros, crear_miembro, obtener_miembro, actualizar_miembro, eliminar_miembro

miembro_bp = Blueprint('miembro_bp', __name__, url_prefix='/api/miembros')

miembro_bp.get('/')(listar_miembros)
miembro_bp.post('/')(crear_miembro)
miembro_bp.get('/<uuid:id>')(obtener_miembro)
miembro_bp.put('/<uuid:id>')(actualizar_miembro)
miembro_bp.delete('/<uuid:id>')(eliminar_miembro)
