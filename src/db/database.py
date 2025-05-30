from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)
