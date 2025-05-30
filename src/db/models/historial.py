from src.db.database import db
import uuid

class Historial(db.Model):
    __tablename__ = 'historial'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prestamo_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('prestamos.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())
