x = 2 + 3
print("x: ", x)

def func1(x=10, y=25):
    sum1 = x + y
    prod1 = x * y
    return sum1
    
    
x = 5
y = 10
sum2 = x + y
print(sum2)

print(func1(5,10))

# 4 parts of a function
# 1. function definition
# 2. parameter list (arguments passed in)
# 3. logic or function body
# 4. return statement or function output

# function call sends arguments to the function

result = func1(10, 50)
print(result)

print(func1())
print(func1(10))

# print(func1(1,2,3))


a = float(input("enter a number: "))
b = float(input("enter a second number: "))
print(func1(a, b))

def sumLst(a, b, c, d, e, f):
    return a + b + c + d + e + f
    
def printHello():
    print("hi")
    
    return None
    
    
printHello()
    
print(sumLst(1,2,3,4,5,6))




    




