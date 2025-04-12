from flask import Flask
from flask_cors import CORS
from config.config import app_config
from apis.libros.routes import Libro
from apis.miembros.routes import Miembro

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Habilitar CORS para todas las rutas y orígenes
# Esto permite que el frontend realice solicitudes a la API
CORS(app)


# Definir un manejador de errores para rutas no encontradas
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


def error_servidor(error):
    return "<h1>Error interno del servidor</h1>", 500


@app.route("/")
def principal():
    return "<h1>Bienvenido a mi aplicación con Flask</h1>"


if __name__ == "__main__":
    # Configurar la aplicación Flask con la configuración de desarrollo
    app.config.from_object(app_config["development"])
    # apartado para rutas
    app.register_blueprint(Libro.main, url_prefix="/api/libros")
    app.register_blueprint(Miembro.main, url_prefix="/api/miembros")
    # Registrar los manejadores de errores
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(500, error_servidor)

    # Iniciamos el servidor de Flask, escuchando en el puerto 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
