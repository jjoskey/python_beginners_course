#  задание
#  1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
#  2. Изучите структуру ответа, сравните её с ответом в запросе без params.
#  3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.

#  решение

import requests

response = requests.get('https://api.binance.com/api/v3/ticker/price')

for ticker in response.json():
    if ticker['symbol'] == 'ETHUSDT':
        print(ticker['price'])
