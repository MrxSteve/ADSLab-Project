from src.db.database import db
import uuid

class Ejemplar(db.Model):
    __tablename__ = 'ejemplares'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    libro_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('libros.id'), nullable=False)
    codigo_interno = db.Column(db.String(50), unique=True, nullable=False)
    estado_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('estados_ejemplares.id'), nullable=False)
