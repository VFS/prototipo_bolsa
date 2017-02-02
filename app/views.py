from flask import jsonify, render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api')
def stock():
    stock = [
        {'date': '2010-05-01', 'val': 10},
        {'date': '2010-05-02', 'val': 5},
        {'date': '2010-05-03', 'val': 20},
    ]
    return jsonify(stock)
