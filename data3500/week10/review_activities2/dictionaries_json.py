import json

print("hello")

person = {}
person["name"] = "andy brim"
person["age"] = 39
person["num_kids"] = 4
person["major"] = ["computer science", "finance"]

print(person)
print(person.keys())

print("-------")
for k in person.keys():
    print(person[k])
    

json.dump(person, open("person.json", "w"))


person_dictionary2 = json.load(open("person.json", "r"))
print("person_dictionary2: ", person_dictionary2)


