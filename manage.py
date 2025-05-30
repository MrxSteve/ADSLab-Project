# manage.py
from flask.cli import FlaskGroup
from src.app import create_app
from src.db import db

app = create_app()
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()