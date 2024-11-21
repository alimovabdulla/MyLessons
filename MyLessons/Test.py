import requests
api = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
request = requests.get(api)
data = request.json()
print(data)