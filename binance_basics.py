from pprint import pprint
from string import ascii_uppercase
import requests

ENDPOINT = "http://api.bitcoincharts.com/v1/markets.json"

response = requests.get(ENDPOINT)
#pprint(response.content)

#print(type(response))
data = response.json()
#print(data)
#print(type(data)) #list

for i in data:
    #print(i["currency"])
    market_name = i['symbol']
    currency = i['currency']
    bid = i['bid']
    ask = i['ask']
    high = i['high']
    low = i['low']
    #print(market_name, currency, high, low)

    # if "kraken" in market_name:
    #     kraken_coins = market_name
    #     print(kraken_coins)

