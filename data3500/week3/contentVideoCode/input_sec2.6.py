# input function, getting input from user
response = input("Enter your name: ")
print("Hello ", response)


# input a string
print(type(response))

# input a number: integer or float
age = input("Please enter your age: ")
age = int(age)
print("In one year you will be: ", age + 1)

pi = input("Enter pi: ")
pi = float(pi)
print("pi: ", pi)

# eval function
pi2 = input("Enter pi again: ")
pi2 = eval(pi2)
print("pi2: ", pi2)
print(type(pi2))

