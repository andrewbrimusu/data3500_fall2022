# 1. Create a function that adds 2 numbers and returns the result.

#  - Create another function which multiplies two numbers, by calling add2nums() (that you created above) in a for loop

# - Create another function which takes an exponent of two numbers by calling mult2nums() (that you created above) in a for loop

# Then sing "The power of love" by Huey Lewis et. al and replace "love" with "functions"


def exponent(num1, num2):
    tot = 1
    for i in range(num2):
        tot = multiply(tot, num1) 
    return tot
    
def multiply(num1, num2):
    tot = 0
    for i in range(num2):
        tot = add(tot, num1) 
    return tot
    
def add(num1, num2):
    return num1 + num2
    
    
print(exponent(2, 10000))

print("--------")

print(2 ** 10000)


#x = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2