from flask import Blueprint
from src.api.multas.controller import listar_multas, crear_multa, obtener_multa, actualizar_multa, eliminar_multa

multa_bp = Blueprint('multa_bp', __name__, url_prefix='/api/multas')

multa_bp.get('/')(listar_multas)
multa_bp.post('/')(crear_multa)
multa_bp.get('/<uuid:id>')(obtener_multa)
multa_bp.put('/<uuid:id>')(actualizar_multa)
multa_bp.delete('/<uuid:id>')(eliminar_multa)
