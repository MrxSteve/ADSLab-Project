from utils.DateFormat import DateFormat


class Miembro:
    def __init__(
        self, id_miembro, nombre, apellido, direccion, telefono, email, fecha_registro
    ):
        self.id_miembro = id_miembro
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_registro = DateFormat.convert_date(fecha_registro)

    def to_JSON(self):
        return {
            "id_miembro": self.id_miembro,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "fecha_registro": self.fecha_registro,
        }
