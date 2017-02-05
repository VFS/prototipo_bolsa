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


cblc_data = CBLC()
cblc_data.init()


def create_response(stock, start_date, end_date):
    print('Request for: %s from: %s to: %s' % (stock, start_date, end_date))
    # yahoo finance uses a sufix to identify the market BOVESPA is .sa
    if stock[-3:] != '.sa':
        stock = stock + '.sa'

    stock = Share(stock)
    print('Stock info: ' + stock.get_name())
    stock = stock.get_historical(start_date, end_date)
    stock.reverse()

    cdi_data = CDI()
    cdi_data.populate_CDI_by_range(start_date, end_date)

    response = cdi_data.get()
    return stock


def create_cblc(stock):
    return cblc_data.get()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/<stock>/<start_date>/<end_date>.json')
def build_stock_cdi_json(stock, start_date, end_date):
    return jsonify(create_response(stock, start_date, end_date))


@app.route('/api/<stock>/cblc.json')
def build_cblc_json(stock):
    return jsonify(create_cblc('asddsa'))
