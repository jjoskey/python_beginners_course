import requests
import json


response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
content = response.content
print(content)
print(type(content))
bitcoin_price = json.loads(content)
print(type(bitcoin_price))
print(bitcoin_price)

response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
bitcoin_price = response.json()["price"]
print(bitcoin_price)
print(type(bitcoin_price))
bitcoin_price = float(bitcoin_price)
price = round(bitcoin_price, 2)
print(price)




import time


bitcoin_prices = []
for _ in range(30):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    price = float(response.json()["price"])
    price = round(price, 2)
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
