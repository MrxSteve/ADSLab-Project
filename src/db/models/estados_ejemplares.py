from src.db.database import db
import uuid

class EstadoEjemplar(db.Model):
    __tablename__ = 'estados_ejemplares'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(50), nullable=False)
