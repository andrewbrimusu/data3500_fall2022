import json

results = {}
results["prices"] = [34.5, 45.3, 56.5, 39.9, 40.5, 43.1]
results["ticker"] = "AAPL"
results["profit"] = 10.43
results["returns"] = 17.5

json.dump(results, open("results.json", "w"))