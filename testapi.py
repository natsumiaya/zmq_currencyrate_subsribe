import urllib
import json
import requests

#using Json Rates
from urllib import urlopen

url = urlopen('http://jsonrates.com/get/?from=IDR&to=USD&apiKey=jr-9ad516c8b5a8d4e15065d8251c947552').read()

result = json.loads(url)
print 'IDR to USD rates:', result['rate']

# Using OpenExchangeRates. WARNING! Base modification not allowed
# from urllib import urlopen
#
# url = urlopen('http://openexchangerates.org/api/latest.json?app_id=1f3e1f53fcec4253aff164f85be128bb&base=IDR').read()
#
# print url
#
# result = json.loads(url)
# print 'IDR rates:', result['rates']['USD']