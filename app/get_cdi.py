import urllib.request
from datetime import date, datetime, timedelta


base_url = 'ftp://ftp.cetip.com.br/IndiceDI/'


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




def get_CDI_by_range(start, end):
	start = datetime.strptime(start, '%Y-%m-%d')
	#start = date(2017, 1, 26)
	end = datetime.strptime(end, '%Y-%m-%d')
	#end = datetime(2017, 2, 10)
	delta = timedelta(days=1)
	d = start
	diff = 0

	weekend = set([5, 6])
	while d <= end:
		if d.weekday() not in weekend:
			print(d.strftime('%Y-%m-%d' + ': ' + get_CDI_by_date(d)))
			diff += 1
		d += delta

print(get_CDI_by_range('2016-02-10','2017-02-10'))