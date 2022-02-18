import json

my_hobbies = {}
my_hobbies["sports"] = ["rugby", "football", "basketball", "soccer"]
my_hobbies["arts"] = ["music", "painting"]
my_hobbies["tv_shows"] = ["the office", "press your luck"]

print(my_hobbies)

json.dump(my_hobbies, open("my_hobbies.json", "w"))


d1 = json.load(open("my_hobbies.json", "r"))
print(d1)



#checkpoint activity
# 1. create a dictionary called personal_info
# 2. Add your name, age, and major to the dictionary
# 3. save the dictionary as a json file
# 4. reload the json file back as a new dictionary
# 5. using a for loop, iterate through the keys of the dictionary and print the values
























# solution
import json

personal_info = {}
personal_info["name"] = "andy"
personal_info["age"] = 39
personal_info["major"] = "data analytics"

json.dump(personal_info, open("person_info.json", "w"))

new_dictionary = json.load(open("person_info.json", "r"))

for key in new_dictionary.keys():
    print(new_dictionary[key])
    
    
    
    






