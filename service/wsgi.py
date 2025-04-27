from flask import Flask
from config import Config
from services import UsersService
from repositories import UsersRepository

from extensions import db

app: Flask = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/')
def index():
    users_service = UsersService(UsersRepository())
    print(users_service.list().fetchall())

    return "Hello, World!"


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
