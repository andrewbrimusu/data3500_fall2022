import requests
import json
import time
import os
    
def append():
    # 1. connect to the following web json api url: https://api.datamuse.com/words?ml=duck&sp=b*&max=5
    #  - download the json
    #  - convert it to a Python dictionary
    #  - save it to a json file permanently
    
    # 2. starting with the code you wrote in the programming activity 1
    #  - go through the python dictionary and take all of the scores (each word has a score)
    #  - append the score to a list, and print the average of the list
    
    # [{"word": "bird", "score": 67510, "tags": ["n"]}, 
        # {"word": "bugger", "score": 57534, "tags": ["n"]}, 
        # {"word": "brunt", "score": 52433, "tags": ["n"]}]
    
    ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    req = requests.get(url)
    time.sleep(12)
    
    req_dict = json.loads(req.text)
    
    print(req_dict.keys())
    
    key1 = "Time Series (Daily)" # dictionary with all prices by date
    key2 = '4. close'
    
    # checking to see if file exists, or if its empty
    # size = os.path.size(ticker + ".csv")
    # if size == 0: # file exists, but is empty
    #     print("file exists, but is empty")
    # if not os.path.exists(ticker + ".csv"): # file does not exist
    #     print("file does not exist")
        
    # opening file and getting the last date
    # this will be used to know what dates, to add data to the file
    csv_file = open(ticker + ".csv", "r")
    lines = csv_file.readlines()
    last_date = lines[-1].split(",")[0]
    
    new_lines = []
    for date in req_dict[key1]:
        if date == last_date:
            break
        print(date + "," + req_dict[key1][date][key2]) #print key, value
        new_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
        
    new_lines = new_lines[::-1]
    csv_file = open(ticker + ".csv", "a") # opening the file to append data
    csv_file.writelines(new_lines) # appending new data
    csv_file.close()
