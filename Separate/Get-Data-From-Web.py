import requests
arz = "USD"
result = requests.get("https://www.blockchain.com/ticker")
a = result.json()[arz]["15m"]
b = result.json()[arz]['last']
c = result.json()[arz]['buy']
d = result.json()[arz]['sell']

print('15m :',a)
print('last :',b)
print('buy :',c)
print('sell :',d)
