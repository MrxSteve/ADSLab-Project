from src.db.database import db
import uuid

class Renovacion(db.Model):
    __tablename__ = 'renovaciones'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prestamo_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('prestamos.id'), nullable=False)
    fecha_renovacion = db.Column(db.Date, nullable=False)
