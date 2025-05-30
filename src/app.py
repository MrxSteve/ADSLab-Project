from flask import Flask
from flask_cors import CORS
from src.config.config import app_config
from src.db.database import init_app
from flasgger import Swagger

# Importaciones de las Rutas
from src.api.estados.routes import estado_bp
from src.api.estados_ejemplares.routes import estado_ejemplar_bp
from src.api.miembros.routes import miembro_bp
from src.api.libros.routes import libro_bp
from src.api.ejemplares.routes import ejemplar_bp
from src.api.fechas.routes import fecha_bp
from src.api.prestamos.routes import prestamo_bp
from src.api.multas.routes import multa_bp
from src.api.renovaciones.routes import renovacion_bp
from src.api.historial.routes import historial_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config['development'])

    init_app(app)
    CORS(app)
    Swagger(app)

    # Rutas
    app.register_blueprint(estado_bp)
    app.register_blueprint(estado_ejemplar_bp)
    app.register_blueprint(miembro_bp)
    app.register_blueprint(libro_bp)
    app.register_blueprint(ejemplar_bp)
    app.register_blueprint(prestamo_bp)
    app.register_blueprint(fecha_bp)
    app.register_blueprint(multa_bp)
    app.register_blueprint(renovacion_bp)
    app.register_blueprint(historial_bp)

    # Errores
    app.register_error_handler(404, lambda e: ("Page not found", 404))
    app.register_error_handler(500, lambda e: ("Internal server error", 500))

    @app.route('/')
    def principal():
        return "Welcome to the Flask API!"

    return app