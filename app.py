from flask import Flask, request, redirect, render_template
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model.models import *
from controller.User import UserController
from admin.Admin import start_views


config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='view\templates', static_folder='view\static')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ativar área administrativa
    start_views(app, db)

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'
    
    @app.route('/login')
    def login():
        return 'Tela de login'
    
    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        result = user.login(email, password)

        if result:
            return redirect('/admin')
        else:
            return render_template('login.html', data={'status':401, 'msg': 'Dados de usuário incorretos', 'type': None})

    @app.route('/recovery-password')
    def recovery_password():
        return 'Tela de recuperação de senha'
    
    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()

        result = user.recovery(request.form['email'])

        if result:
            return render_template('recovery.html', data={'status':200, 'msg': 'E-mail de recuperação enviado com sucesso'})
        else:
            return render_template('recovery.html', data={'status':401, 'msg': 'Erro ao enviar e-mail de recuperação'})
    
    return app