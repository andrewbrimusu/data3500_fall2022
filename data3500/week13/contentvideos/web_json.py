import requests
import json

    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
print(url)
request = requests.get(url)
# print(request.text)

rqst_dict = json.loads(request.text)
print(rqst_dict)

json.dump(rqst_dict, open(ticker+".csv", "w"))


# checkpoing activity
# - connect to the following web json api url: https://api.datamuse.com/words?ml=duck&sp=b*&max=3
# - download the json
# - convert it to a Python dictionary
# - save it to a json file permanently

















# solution
url = "https://api.datamuse.com/words?ml=duck&sp=b*&max=3"
request = requests.get(url) # going to website to get json as a string
dict = json.loads(request.text) # convert json to dictionary
json.dump(dict, open("words.json", "w"))
