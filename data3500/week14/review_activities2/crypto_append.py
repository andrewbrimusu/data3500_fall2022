import requests
import json
import time
from datetime import datetime, timedelta

# append script should be run after new data exists
# i.e. run crypto_new_data.py first

url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-11-2020&localization=false"
req = requests.get(url)
print(req.text)

url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

key1 = 'market_data'
key2 = 'current_price'
key3 = 'usd'

dt = datetime(2020, 11, 20)

coins = ["ripple"] 
for coin in coins:
    file = open(coin + ".csv", "r")
    # file.write("Date," + coin + "\n")
    last_date_str = file.readlines()[-1].split(",")[0]
    last_dt = datetime.strptime(last_date_str, '%d-%m-%Y')
    current_date = datetime.now()
    
    file.close()
    file = open(coin + ".csv", "a")
    for i in range(364):
        dt += timedelta(days=1)
        if dt > current_date:
            break
        
        dts = dt.strftime("%d-%m-%Y")
        url = url1 + coin + url2 + dts + url3
        req = requests.get(url)
        time.sleep(1)
        d = json.loads(req.text)
        # try:
        print(dts, d[key1][key2][key3])
        
        if dt > last_dt and dt <= current_date:
            file.write(dts + "," + str(d[key1][key2][key3]) + "\n")


        # except:
            # pass
            # print(d)
            
file.close()
