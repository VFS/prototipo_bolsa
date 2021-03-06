import urllib.request
from datetime import datetime, timedelta


base_url = 'ftp://ftp.cetip.com.br/IndiceDI/'


class CDI:
    # CDI data will live on a dict
    cdi_dict = dict()
    sup = 'dsa'

    def get(self):
        return self.cdi_dict

    # Fetch a file from a specific day and return it's data as a dict
    def get_CDI_by_date(self, d):
        day = d.strftime('%Y%m%d')
        url = base_url + day + '.txt'

        try:
            data = urllib.request.urlopen(url)
            content = data.read()
            cdi = int(content.strip().decode()) * 0.01
            cdi = format(cdi, '.2f')
            self.cdi_dict[d.strftime('%Y-%m-%d')] = cdi

        except:
            print('Deu ruim')

    # iterates trough a date range, ignoring weekends
    def populate_CDI_by_range(self, start, end):
        # print(start)
        # print(end)
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')

        if end > datetime.today():
            end = datetime.today()
            # print("You can't fetch future information!")

        delta = timedelta(days=1)
        d = start
        diff = 0

        weekend = set([5, 6])  # Saturday and Sunday
        while d <= end:
            if d.weekday() not in weekend:
                # print(d.strftime('%Y-%m-%d' + ': ' + get_CDI_by_date(d)))
                self.get_CDI_by_date(d)
                diff += 1
            d += delta
