import numpy
import json

tickers = ["ADBE", "GOOG", "CCL"]
results = {}
for ticker in tickers:
    file = open("/home/ec2-user/environment/week11/zoomsession2/" + ticker + ".txt")
    lines = file.readlines()
    prices = []
    for line in lines:
        prices.append(float(line))
    
    results[ticker + "_prices"] = prices
    results[ticker + "_avg"] = numpy.mean(prices)
    
print(results)
json.dump(results, open("results.json", "w"))
    
