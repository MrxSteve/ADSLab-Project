from flask import Blueprint, jsonify, request
import uuid  # que lo usaremos para generarlos en Postgres
from ..models.LibrosModels import LibroModel
from ..models.entities.Libros import Libro
from datetime import datetime  # para manejar las fechas

main = Blueprint("libro_blueprint", __name__)


@main.route("/", methods=["GET"])
def get_libros():
    try:
        libros = LibroModel.get_all_libros()
        if libros:
            return jsonify(libros), 200
        else:
            return jsonify({"message": "No hay libros disponibles"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/<id>", methods=["GET"])
def get_libro_by_id(id):
    try:
        libro = LibroModel.get_libro_by_id(id)
        if libro:
            return jsonify(libro), 200
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_libro():
    try:
        data = request.get_json()
        require_fields = ["titulo", "autor", "editorial", "anio_publicacion", "genero"]
        missing_fields = [field for field in require_fields if field not in data]
        if missing_fields:
            return (
                jsonify(
                    {"error": f"Faltan campos requeridos: {', '.join(missing_fields)}"}
                ),
                400,
            )
        libro_id = str(uuid.uuid4())
        libro = Libro(
            id_libro=libro_id,
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            editorial=data.get("editorial"),
            anio_publicacion=data.get("anio_publicacion"),
            genero=data.get("genero"),
        )
        LibroModel.add_libro(libro)
        return jsonify({"message": "Libro agregado exitosamente", "id": libro_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_libro(id):
    try:
        data = request.get_json()
        existing_libro = LibroModel.get_libro_by_id(id)
        if not existing_libro:
            return (
                jsonify({"error": "Libro no encontrado"}),
                404,
            )
        required_fields = ["titulo", "autor", "editorial", "anio_publicacion", "genero"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify(
                    {"error": f"Faltan campos requeridos: {', '.join(missing_fields)}"}
                ),
                400,
            )
        libro = Libro(
            id_libro=id,
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            editorial=data.get("editorial"),
            anio_publicacion=data.get("anio_publicacion"),
            genero=data.get("genero"),
        )
        affected_rows = LibroModel.update_libro(libro)
        if affected_rows == 1:
            return jsonify({"message": "Libro actualizado exitosamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el libro"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_libro(id):
    try:
        libro = Libro(
            id_libro=id,
            titulo="",
            autor="",
            editorial="",
            anio_publicacion="",
            genero="",
        )
        affected_rows = LibroModel.delete_libro(libro)
        if affected_rows == 1:
            return jsonify({"message": f"Libro {id} eliminado exitosamente"})
        else:
            return jsonify({"error": "Libro no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
