from flask import Blueprint, jsonify, request
import uuid
from ..models.MiembrosModels import MiembroModel
from ..models.entities.Miembros import Miembro
from datetime import datetime

main = Blueprint("miembro_blueprint", __name__)


@main.route("/", methods=["GET"])
def get_miembros():
    try:
        miembros = MiembroModel.get_all_miembros()
        if miembros:
            return jsonify(miembros), 200
        else:
            return jsonify({"message": "No se encontraron miembros"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/<id>", methods=["GET"])
def get_miembro_by_id(id):
    try:
        miembro = MiembroModel.get_miembro_by_id(id)
        if miembro:
            return jsonify(miembro)
        else:
            return jsonify({"error": "No se encontró el miembro"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_miembro():
    try:
        data = request.get_json()
        required_fields = ["nombre", "apellido", "direccion", "telefono", "email", "fecha_registro"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify(
                    {
                        "error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"
                    }
                ),
                400,
            )
        miembro_id = str(uuid.uuid4())
        fecha_reg_str = data.get(
            "fecha_registro", datetime.now().strftime("%d/%m/%Y")
        )
        fecha_nac_object = datetime.strptime(fecha_reg_str, "%d/%m/%Y")
        miembro = Miembro(
            id_miembro=miembro_id,
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            email=data.get("email"),
            fecha_registro=fecha_nac_object,
        )
        MiembroModel.add_miembro(miembro)
        return (
            jsonify({"message": "Miembro agregado exitosamente", "id": miembro_id}),
            201,
        )
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_miembro(id):
    try:
        data = request.get_json()
        existing_miembro = MiembroModel.get_miembro_by_id(id)
        if not existing_miembro:
            return jsonify({"error": "No se encontró el miembro"}), 404
        required_fields = [
            "nombre",
            "apellido",
            "direccion",
            "telefono",
            "email",
            "fecha_registro",
        ]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify(
                    {
                        "error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"
                    }
                ),
                400,
            )
        fecha_reg_str = data.get("fecha_registro")
        fecha_reg_object = datetime.strptime(fecha_reg_str, "%d/%m/%Y")
        miembro = Miembro(
            id_miembro=id,
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            email=data.get("email"),
            fecha_registro=fecha_reg_object,
        )
        affected_rows = MiembroModel.update_miembro(miembro)
        if affected_rows == 1:
            return jsonify({"message": "Miembro actualizado exitosamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el miembro"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_miembro(id):
    try:
        miembro = Miembro(
            id_miembro=id,
            nombre="",
            apellido="",
            direccion="",
            telefono="",
            email="",
            fecha_registro=datetime.now()
        )
        affected_rows = MiembroModel.delete_miembro(miembro)
        if affected_rows == 1:
            return jsonify({"message": f"Miembro {id} eliminado"}), 200
        else:
            return jsonify({"error": "Miembro no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
