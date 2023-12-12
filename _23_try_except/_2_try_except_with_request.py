import requests

try:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    bitcoin_price = response.json()["price"]
    price = float(bitcoin_price)
    print(price)
except requests.exceptions.ConnectionError as error:
    print(f"Something goes wrong: {error}")
