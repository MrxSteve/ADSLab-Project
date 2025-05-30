from src.db.database import db
import uuid

class Miembro(db.Model):
    __tablename__ = 'miembros'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
