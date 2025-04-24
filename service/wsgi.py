from flask import Flask
from config import Config

app: Flask = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
