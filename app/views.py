from flask import jsonify, render_template
from yahoo_finance import Share
from app import app


# We create a Share object based on the Symbol we want
dtex = Share('dtex3.sa')

# list of dicts with historical data
s_h = dtex.get_historical('2016-11-11', '2017-01-20')

# The list comes in decrescent order, so we need to reverse
s_h.reverse()

# date = ['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05']
# date.insert(0, 'Date')

# stock = [30, 200, 100, 400, 150]
# stock.insert(0, 'Stock')

# cdi = [50, 400, 14, 40, 30]
# cdi.insert(0, 'CDI')


# response = [date, stock, cdi]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api')
def stock():
    return jsonify(s_h)
