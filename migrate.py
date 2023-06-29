from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from app import create_app, db
from config import app_config, app_active

config = app_config[app_active]

app = create_app(app_active)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()

    ## $env:FLASK_APP = "app:create_app('development')"
    ## flask db init, flask db migrate, flask db upgrade