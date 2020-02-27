import requests
from prettytable import PrettyTable

r = requests.get("https://api.coinmarketcap.com/v1/ticker/")
data = r.json()

x = PrettyTable()
x.field_names = [ "Crypto Name", "Symbol", "Price in USD"]

for crypto in data:
    x.add_row([ crypto['name'], crypto['symbol'], crypto['price_usd'] ])

print(x)
