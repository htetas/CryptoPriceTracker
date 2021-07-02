import urllib.request, urllib.parse, urllib.error
import json
import ssl
from api import API_KEY #importing API Key stored as API_KEY in api.py

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "https://api.nomics.com/v1/currencies/ticker?"

while True:
    ticker = input('Enter Ticker (Put commas (without space) for mutiple tickers): ') #getting ticker from user
    if len(ticker) < 1: break #stopping the program if user did not put in ticker
    url = serviceurl + 'key=' + API_KEY + '&ids=' + ticker.upper() #getting url to request JSON
    print("Requesting data from www.nomics.com")
    print()
    uh = urllib.request.urlopen(url, context=ctx) #requesting data
    data = uh.read().decode() #reading and decoding data
    try:
        js = json.loads(data)
    except:
        js = None
    if not js:
        print('fail to retrieve data')
        continue
    print("Request Succeeded")
    print()
    for line in js:
        print("Ticker: " + line['id'])
        print("Name: " + line['name'])
        print("Price: " + line['price'] + " USD")
        print("Rank: " + line['rank'])
        print()
    print("Crypto Market Cap & Pricing Data Provided By Nomics(https://nomics.com)")
