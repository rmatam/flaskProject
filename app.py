from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/index')
def index():  # put application's code here
    return 'Welcome to the course!!!'


if __name__ == '__main__':
    app.run()
