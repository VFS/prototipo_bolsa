from flask import jsonify, render_template
from yahoo_finance import Share
from app import app


# We create a Share object based on the Symbol we want
dtex = Share('dtex3.sa')

# list of dicts with historical data
s_h = dtex.get_historical('2016-11-11', '2017-01-20')

# The list comes in decrescent order, so we need to reverse
s_h.reverse()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/<stock>/<start_date>/<end_date>.json')
def build_json(stock, start_date, end_date):
    return jsonify(s_h)
