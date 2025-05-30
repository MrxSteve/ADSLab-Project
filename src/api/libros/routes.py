from flask import Blueprint
from src.api.libros.controller import listar_libros, crear_libro, obtener_libro, actualizar_libro, eliminar_libro

libro_bp = Blueprint('libro_bp', __name__, url_prefix='/api/libros')

libro_bp.get('/')(listar_libros)
libro_bp.post('/')(crear_libro)
libro_bp.get('/<uuid:id>')(obtener_libro)
libro_bp.put('/<uuid:id>')(actualizar_libro)
libro_bp.delete('/<uuid:id>')(eliminar_libro)
