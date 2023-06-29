import os
import random, string

class Config(object):
    # Habilita o uso de criptografia em sessões do Flask
    CSRF_ENABLED = True
    
    # Será usada em alguns momentos para criar chaves e valores criptografados
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%l2bck*gn@w3@f&-&'

    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    # Habilita exibição de recursos de warning e erros
    TESTING = True

    # Habilita log na tela do terminal
    DEBUG = True
    
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')