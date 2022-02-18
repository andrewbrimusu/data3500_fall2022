user_age = input("whats your age: ")
user_fav_color = input("what's your favorite color: ")

person = {}

person["age"] = user_age
person["favorite_color"] = user_fav_color

for key in person.keys():
    print(key, ":", person[key])
    