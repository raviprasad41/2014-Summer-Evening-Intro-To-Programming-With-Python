import urllib2

url = "http://api-sandbox.oanda.com/v1/candles?instrument=EUR_USD&start=2014-06-19T15%3A00%3A00Z&end=2014-06-19T15%3A59%3A00Z"
u = urllib2.urlopen(url)
data = u.read()

f = open("sandbox.json", 'w')

f.write(data)

