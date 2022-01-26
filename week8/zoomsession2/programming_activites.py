# get user age
age = int(input("Hi!!! Please enter your age: "))

# get user favorite color
favorite_color = input("Please enter your favorite color: ")

user_info = {}
user_info["age"] = age # something
user_info["favorite_color"] = favorite_color# something

for key in user_info.keys():
    print(user_info[key])
    
    
import numpy

np1 = numpy.zeros(100)
np1 = np.random.randint(10, size=100)

print("np1: ", np1)

