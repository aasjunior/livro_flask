import sys
from app import create_app, db
from config import app_config, app_active

config = app_config[app_active]
app = create_app(app_active)

if __name__ == '__main__':
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys)