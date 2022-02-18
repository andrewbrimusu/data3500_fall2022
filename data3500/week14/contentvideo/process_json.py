import requests
import json

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

req_dict = json.loads(req.text)

print(req_dict.keys())

key1 = "Time Series (Daily)" # dictionary with all prices by date
key2 = '4. close'

csv_file = open(ticker + ".csv", "w")
csv_file.write("Date,AAPL\n")
write_lines = []
for date in req_dict[key1]:
    print(date + "," + req_dict[key1][date][key2]) #print key, value
    # csv_file.write(date + "," + req_dict[key1][date][key2]+"\n") #print key, value
    write_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
    
write_lines = write_lines[::-1]
csv_file.writelines(write_lines)
csv_file.close()
