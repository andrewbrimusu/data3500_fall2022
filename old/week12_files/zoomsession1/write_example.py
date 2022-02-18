import json
# Programming Activities:

# 1. Write a program, and have the user enter their name and their favorite color, as two separate variables.  Write the sentence to a file using the with command "<name>'s favorite color is <color>"

# - get two variables from user

# - use the with command to open the file

# - use the write function to write to the file

nam = input("Enter your name: ")
col = input("Enter your favorite color: ")

with open("info.txt", "w") as fil:
    fil.write(nam + "\n")
    fil.write(col + "\n")
    
    
# 2. Write a program, which loads a json file "person.json" into a Python dictionary.  Change the contents of person["age"] by adding 1.  Save the updated dictionary to person.json, and verify the contents of person.json have been updated.

# - load person.json in to a Python dictionary using the json.load() function

# - update the value of person["age"], increase by 1

# - save the Python dictionary to person.json

# - open person.json and verify the "age" value has increased by 1


dictionary1 = json.load(open("person.json"))

dictionary1["age"] += 1

json.dump(dictionary1, open("person.json", "w"))


