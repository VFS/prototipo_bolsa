from flask import jsonify, render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api')
def stock():
    stock = {
        'data1': [1, 2, 3],
        'data2': [2, 3, 3],
        'data3': [4, 1, 1]
    }
    return jsonify(stock)
