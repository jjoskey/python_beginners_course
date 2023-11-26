import requests

response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
content = response.content
print(content)
print(type(content))
price_object = response.json()
price = float(price_object['price'])

import time

bitcoin_prices = []
for i in range(30):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    price = float(response.json()["price"])
    price = round(price, 2)
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
