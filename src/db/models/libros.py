from src.db.database import db
import uuid

class Libro(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(100))
    editorial = db.Column(db.String(100))
    genero = db.Column(db.String(50))
