import requests
import json
import numpy
    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
request = requests.get(url)
rqst_dictionary = json.loads(request.text)

key1 = "Time Series (Daily)"
# date, i need all dates
key2 = "4. close"

fil = open(ticker + ".csv", "w")
fil.write("Date,prices\n")

for date in rqst_dictionary[key1]:
    fil.write(date + "," + rqst_dictionary[key1][date][key2] + "\n")
    
fil.close()




# checkpoint activity
# - starting with the code you wrote in the web_json.py checkpoint activity
# - go through the python dictionary and take all of the scores (each word has a score)
# - append the score to a list, and print the average of the list






























# solution
url = "https://api.datamuse.com/words?ml=duck&sp=b*&max=3"
request = requests.get(url)
dict = json.loads(request.text)

scores = []
for d in dict:
    scores.append(d["score"])
print("scores: ", scores)
print("avg score: ", numpy.mean(#something))