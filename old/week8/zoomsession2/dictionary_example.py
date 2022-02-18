import json

lst = [95.0, 89.3, 92.9, 94.5]
print(lst)

print(lst[0])


dictionary1 = {}
dictionary1["name"] = "andy"
dictionary1["age"] = 40
dictionary1["grades"] = [95.0, 89.3, 92.9, 94.5]
# dictionary1[5] = 100

# key value pair

def birthday(d, s):
    d["age"] += 1
    s = "having more fun!!!!"
    
print(dictionary1)

havingFun = "yes!!!!"
birthday(dictionary1, havingFun)
print(dictionary1["age"])
print(havingFun)

print(id(havingFun))
havingFun = "having lots of fun!!!!"
print(id(havingFun))

print(havingFun)

for item in lst:
    print(item)
    
for item in dictionary1:
    print(item, ":", dictionary1[item])
    
for item in dictionary1.keys():
    print(item, ":", dictionary1[item])
    
json.dump(dictionary1, open("results.json", "w"))

dictionary2 = json.load(open("results.json"))
print(dictionary2)
    
    