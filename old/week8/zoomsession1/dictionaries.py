import json

ages = [22, 32, 21, 21, 4, 22]
favorite_colors = ["blue", "green", "purple", "gree", "cumquat"]

lst_bad_style = [30, "hi", "float", 3.1415]

print(lst_bad_style)

new_list = []

person = {}

person["age"] = 39
person["favorite_color"] = "aggie blue"
person["gpa"] = 3.74
person["enjoys_outdoors"] = True

print("person: ", person)
print(person["age"])
person["age"] += 1
print(person["age"])

my_age = 39
my_favorite_color = "aggie blue"
my_gpa = 3.74
enjoys_outdoors = True

mr_final_profit_percentage = 0.42

results = {}
ticker = "ADBE"

results[ticker + "_mr_final_profit_percentage"] = 0.42

print(results)

json.dump(results, open("results.json", "w"))

print("------")
for key in person.keys():
    print(key, person[key])
    


results = {}
tickers = ["AAPL", "GOOG", "ADBE"]
strategies = ["mr", "sma"]

for ticker in tickers:
    for strategy in strategies:
        results[ticker + "_" + strategy + "_" + "profit"] = 0.0 # your program will call the strategy function to get the results
        
for key in results.keys():
    print(key, ":", results[key])
    