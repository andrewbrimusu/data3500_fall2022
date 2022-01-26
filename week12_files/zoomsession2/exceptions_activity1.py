# 1. Write a program that asks the user for two numbers.  In a try statement, attempt to divide number 1 by number 2.  If number 2 is a 0, print a message in the except statement saying "Error, attempted to divide by zero"

# - create two variables, inputted by the user

# - in a  try: block attempt to divide num1 by num2

# - in a except: block print a message indicating divide by zero error

# - end program

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

try:
    print(num1 / num2)
    
except:
    print("Divide by Zero!!")
    
print("program over")