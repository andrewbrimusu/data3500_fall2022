def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    tot = 0
    for i in range(num2):
        tot = add(tot, num1)
        
    return tot
        

def exponent(num1, num2):
    tot = 1
    for i in range(num2):
        tot = multiply(tot, num1)
        
    return tot
    
    
# print(add(3,5))
# print(multiply(3,5))
# print(exponent(3,5))


print(exponent(2,2048))

