from src.db.database import db
import uuid

class Multa(db.Model):
    __tablename__ = 'multas'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prestamo_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('prestamos.id'), nullable=False)
    monto = db.Column(db.Numeric(10,2), nullable=False)
    descripcion = db.Column(db.Text)
    pagada = db.Column(db.Boolean, default=False)
