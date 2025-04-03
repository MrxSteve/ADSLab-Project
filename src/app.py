from flask import Flask
from flask_cors import CORS
from config.config import app_config

app = Flask(__name__)

CORS(app)

def pageNotFound(e):
    return "Page not found", 404

def internalServerError(e):
    return "Internal server error", 500

@app.route('/')
def principal():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.config.from_object(app_config['development'])

    app.register_error_handler(404, pageNotFound)
    app.register_error_handler(500, internalServerError)

    app.run(host='0.0.0.0', port=5000, debug=True)