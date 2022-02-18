import requests
import json
    
def create_data():
    ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    print(url)
    request = requests.get(url)
    rqst_dict = json.loads(request.text)
    
    key_series = "Time Series (Daily)"
    key_open = '1. open'
    key_close = '4. close'
    key_hi = '2. high'
    key_lo = '3. low'
    
    
    prices = []
    
    for date in rqst_dict[key_series]:
        row = ""
        row += date + ","
        row += rqst_dict[key_series][date][key_open] + ","
        row += rqst_dict[key_series][date][key_hi] + ","
        row += rqst_dict[key_series][date][key_lo] + ","
        row += rqst_dict[key_series][date][key_close] + "\n"
        
        prices.append(row)
        
    prices.reverse()
    
    # print(prices)    
    
    csv_file = open(ticker + ".csv", "w")
    csv_file.write("date,open,hi,lo,close\n")
    
    for row in prices:
        csv_file.write(row)
        
    csv_file.close()
    
    
    
    
def append_data():
    #this function appends new data, hooray!
    ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    print(url)
    request = requests.get(url)
    rqst_dict = json.loads(request.text)
    # print(rqst_dict)
    
    key_series = "Time Series (Daily)"
    key_open = '1. open'
    key_close = '4. close'
    key_hi = '2. high'
    key_lo = '3. low'
    
    # get the last day, of data
    file = open(ticker + ".csv")
    lines = file.readlines()
    last_line = lines[-1]
    items = last_line.split(",")
    last_date = items[0]
    
    # last_date = open(ticker + ".csv").readlines()[-1].split(",")[0]
    
    prices = []
    
    for date in rqst_dict[key_series]:
        row = ""
        row += date + ","
        row += rqst_dict[key_series][date][key_open] + ","
        row += rqst_dict[key_series][date][key_hi] + ","
        row += rqst_dict[key_series][date][key_lo] + ","
        row += rqst_dict[key_series][date][key_close] + "\n"
        if date > last_date:
            prices.append(row)
        
    prices.reverse()
    
    # print(prices)    
    
    csv_file = open(ticker + ".csv", "a")
    
    for row in prices:
        csv_file.write(row)
        
    csv_file.close()
    
    
# create_data()

append_data()
    
