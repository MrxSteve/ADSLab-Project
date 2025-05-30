from src.db.database import db
import uuid

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    miembro_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('miembros.id'), nullable=False)
    ejemplar_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('ejemplares.id'), nullable=False)
    estado_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('estados.id'), nullable=False)
