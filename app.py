from flask import Flask
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

config = app_config[app_active]
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, template_folder='template')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app
