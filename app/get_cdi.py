import urllib.request
from datetime import datetime, timedelta


base_url = 'ftp://ftp.cetip.com.br/IndiceDI/'


# Fetch a file from a specific day and return it's data as a dict
def get_CDI_by_date(day):
    day = day.strftime('%Y%m%d')
    url = base_url + day + '.txt'

    try:
        data = urllib.request.urlopen(url)
        content = data.read()
        cdi = int(content.strip().decode()) * 0.01
        cdi = format(cdi, '.2f')
        return cdi

    except urllib.error.URLError as e:
        print(e.reason)


# iterates trough a date range, ignoring weekends
def get_CDI_by_range(start, end):
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')
    delta = timedelta(days=1)
    d = start
    diff = 0

    weekend = set([5, 6])  # Saturday and Sunday
    while d <= end:
        if d.weekday() not in weekend:
            print(d.strftime('%Y-%m-%d' + ': ' + get_CDI_by_date(d)))
            diff += 1
        d += delta


print(get_CDI_by_range('2016-02-10','2017-02-10'))
