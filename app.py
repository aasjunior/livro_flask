from flask import Flask, request
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model.models import *

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='view\templates', static_folder='view\static')

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
    
    @app.route('/login')
    def login():
        return 'Tela de login'
    
    @app.route('/recovery-password')
    def recovery_password():
        return 'Tela de recuperação de senha'
    
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id, action):
        if action == 'action1':
            return 'Ação action1 usuário de ID %d' % id
        if action == 'action2':
            return 'Ação action2 usuário de ID %d' % id
        if action == 'action3':
            return 'Ação action3 usuário de ID %d' % id
        
    @app.route('/profile', methods=['POST', 'GET'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']

        if request.method == 'POST':
            return 'Essa rota possui um método POST e criará um usuário com os dados de usuário %s e a senha %s' % (username, password)
        elif request.method == 'GET':
            return 'Método GET sendo requisitado'

    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']

        return 'Essa rota possui um método PUT e editará o nome do usuário para %s e a senha para %s' % (username, password)

    return app