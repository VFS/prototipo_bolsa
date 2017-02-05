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


def create_stock_cdi_response(stock, start_date, end_date):
    print('STOCK + CDI Request for: %s from: %s to: %s' % (stock, start_date, end_date))
    # yahoo finance uses a sufix to identify the market BOVESPA is .sa
    if stock[-3:] != '.sa':
        stock = stock + '.sa'

    stock = Share(stock)
    print('Stock info: ' + stock.get_name())
    stock = stock.get_historical(start_date, end_date)
    stock.reverse()

    cdi_data = CDI()
    cdi_data.populate_CDI_by_range(start_date, end_date)
    r = cdi_data.get()

    response = stock

    cdi_percent = 100 / float(r[start_date])
    print('======')
    print(cdi_percent)
    print('======')
    adj_close_percent = 100 / float(response[0]['Adj_Close'])

    for el in response:
        adj = float(el['Adj_Close'])
        el['Adj_Close_Percent'] = adj * adj_close_percent
        el_date = el['Date']
        el['CDI'] = r[el_date]
        el['CDI_percent'] = float(r[el_date]) * cdi_percent
    print(type(response))
    #print(response)
    #print(r.get())
    return response


def create_stock_response(stock, start_date, end_date):
    print('Request for: %s from: %s to: %s' % (stock, start_date, end_date))
    # yahoo finance uses a sufix to identify the market BOVESPA is .sa
    if stock[-3:] != '.sa':
        stock = stock + '.sa'

    stock = Share(stock)
    print('Stock info: ' + stock.get_name())
    stock = stock.get_historical(start_date, end_date)
    stock.reverse()

    return stock


def create_cblc(stock):
    stock = stock.upper()
    print(stock)
    r = cblc_data.get()
    response = {}
    response['r00'] = r['00'][0]

    for el in r['01']:
        if(el['Acao'] == stock):
            response['r01'] = el

    for el in r['02']:
        if(el['Acao'] == stock):
            response['r02'] = el

    for el in r['03']:
        if(el['Acao'] == stock):
            response['r03'] = el

    return response


def create_cdi(start_date, end_date):
    return 'asd'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/stock_cdi/<stock>/<start_date>/<end_date>/stock_cdi.json')
def build_stock_cdi_json(stock, start_date, end_date):
    return jsonify(create_stock_cdi_response(stock, start_date, end_date))


@app.route('/api/stock/<stock>/<start_date>/<end_date>/stock.json')
def build_stock_json(stock, start_date, end_date):
    return jsonify(create_stock_response(stock, start_date, end_date))


@app.route('/api/cblc/<stock>/cblc.json')
def build_cblc_json(stock):
    return jsonify(create_cblc(stock))


@app.route('/api/cdi/<start_date>/<end_date>/cdi.json')
def build_cdi_json(start_date, end_date):
    return jsonify(create_cdi(start_date, end_date))
