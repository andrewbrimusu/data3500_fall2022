import json

person = {}
person["name"] = "andy"
person["age"] = 39
person["birthday"] = "august 14"

print(person)

json.dump(person, open("person.json", "w"), indent=4)

person1 = json.load(open("person.json"))

print(person1)

person1["age"] += 1
json.dump(person1, open("person.json", "w"), indent=4)


