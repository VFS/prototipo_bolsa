from flask import Flask
app = Flask(__name__)

from app import views


@app.route('/')
def hello_world():
    return 'Hello, World!'
