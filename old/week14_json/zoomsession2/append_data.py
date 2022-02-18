# This is the orignial version of the file.
# in week14 zoomsession2 we updated this python program to append open, high, low, and close prices
# review the zoomsession recording and notes, to see how this is done


import requests
import json
import time
import os
    
def append():

    ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    req = requests.get(url)
    # time.sleep(12)
    
    req_dict = json.loads(req.text)
    
    print(req_dict.keys())
    
    key1 = "Time Series (Daily)" # dictionary with all prices by date
    key2 = '4. close'
    
    csv_file = open(ticker + ".csv", "r")
    lines = csv_file.readlines()
    last_date = lines[-1].split(",")[0]
    
    new_lines = []
    for date in req_dict[key1]:
        if date == last_date:
            break
        print(date + "," + req_dict[key1][date][key2]) #print key, value
        new_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
        
    new_lines.reverse()
    csv_file = open(ticker + ".csv", "a") # opening the file to append data
    csv_file.writelines(new_lines) # appending new data
    csv_file.close()

append()