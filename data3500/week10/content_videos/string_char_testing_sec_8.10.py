
# for isdigit and isalnum every character
# must be a digit or alpha numeric for the
# function to return true

#isdigit
string = "-12341234"
print(string.isdigit())

string = "12341234"
print(string.isdigit())


#isalnum
address = "123 Main St"
print(address.isalnum())


address = "123MainSt"
print(address.isalnum())









# checkpoint activity
# write a program which asks the user to enter their age
# Using isdigit test to see if they actually entered a number






















# solution
age = input("Enter your age: ")
if age.isdigit():
    print("Thanks for entering a number")
else:
    print("You entered something other than a number")
    



