from flask import Blueprint
from src.api.prestamos.controller import listar_prestamos, crear_prestamo, obtener_prestamo, actualizar_prestamo, eliminar_prestamo

prestamo_bp = Blueprint('prestamo_bp', __name__, url_prefix='/api/prestamos')

prestamo_bp.get('/')(listar_prestamos)
prestamo_bp.post('/')(crear_prestamo)
prestamo_bp.get('/<uuid:id>')(obtener_prestamo)
prestamo_bp.put('/<uuid:id>')(actualizar_prestamo)
prestamo_bp.delete('/<uuid:id>')(eliminar_prestamo)
