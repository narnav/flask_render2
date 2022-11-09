from flask import Flask
api = Flask(__name__)


@api.route('/')
def index():
    return 'Hello, World!'


@api.route('/eli')
def eli():
    return 'Hello, eli!'


if __name__ == '__main__':
    api.run(debug=True)
