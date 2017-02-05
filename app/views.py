from flask import jsonify, render_template
from yahoo_finance import Share
from app import app
from app.get_cblc import CBLC
from app.get_cdi import CDI


# We create a Share object based on the Symbol we want
dtex = Share('dtex3.sa')

# list of dicts with historical data
s_h = dtex.get_historical('2016-11-11', '2017-01-20')

# The list comes in decrescent order, so we need to reverse
s_h.reverse()


def create_response(stock, start_date, end_date):
    print('Request for: %s from: %s to: %s' % (stock, start_date, end_date))
    # yahoo finance uses a sufix to identify the market BOVESPA is .sa
    if stock[-3:] != '.sa':
        stock = stock + '.sa'

    stock = Share(stock)
    print('Stock info: ' + stock.get_name())
    response = stock.get_historical(start_date, end_date)
    response.reverse()
    # response = s_h
    # return response
    return response


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/<stock>/<start_date>/<end_date>.json')
def build_json(stock, start_date, end_date):
    return jsonify(create_response(stock, start_date, end_date))
