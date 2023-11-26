import requests
from requests.exceptions import RequestException

response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
bitcoin_price = response.json()["price"]
price = float(bitcoin_price)
print(price)

try:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    bitcoin_price = response.json()["price"]
    price = float(bitcoin_price)
    print(price)
except requests.exceptions.RequestException as error:
    print(f"Something goes wrong: {error}")
