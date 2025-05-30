from src.db.database import db
import uuid

class Fecha(db.Model):
    __tablename__ = 'fechas'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prestamo_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('prestamos.id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date)
