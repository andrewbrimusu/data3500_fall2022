import os
os.system("pip3 install requests")
import requests
import json

    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
req = requests.get(url)

req_dct = json.loads(req.text)
json.dump(req_dct, open("data.json", "w"))