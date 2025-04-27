from flask import Flask
from config import Config
from controllers import list_users_bp

from extensions import db

app: Flask = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(list_users_bp)


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
