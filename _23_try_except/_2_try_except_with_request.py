import requests
from requests.exceptions import RequestException

# response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
# price = float(response.json()["price"])
# price = round(price, 2)
# print(price)


# try:
#     response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
#     price = float(response.json()["price"])
#     price = round(price, 2)
#     print(price)
# except RequestException:
#     print("Something goes wrong")


try:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    price = float(response.json()["price"])
    price = round(price, 2)
    print(price)
except RequestException as error:
    print(f"Something goes wrong: {error}")
