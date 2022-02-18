import requests
import json
import time
from datetime import datetime, timedelta


url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-11-2020&localization=false"
req = requests.get(url)
print(req.text)

url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

key1 = 'market_data'
key2 = 'current_price'
key3 = 'usd'

dt = datetime(2021, 1, 1)

coins = ["bitcoin"]

for coin in coins:
    file = open(coin + ".csv", "a")
    file.write("Date," + coin + "\n")
    for i in range(109): # 109 days in 2021 so far
        dt += timedelta(days=1)
        dts = dt.strftime("%d-%m-%Y")
        
        url = url1 + coin + url2 + dts + url3
        req = requests.get(url)
        time.sleep(2)
        d = json.loads(req.text)
        print(dts, d[key1][key2][key3])
        # add logic to write and flush here.  See zoom recording at time 1:02:00 for this
