# get name and color from user
name = input("what's your name: ")
color = input("what's your favorite color: ")

# using with command open a file "user_info.txt" (or whatever you want)
# inside the with command write the user's info to a file
with open("user_info.txt", "w") as file:
    file.write(name + "'s favorite color is " + color)
