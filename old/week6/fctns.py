
# 4 parts to a function:
# 1. function definition
# 2. parameter list
# 3. function body, or logic
# 4. return statement

def add_2_nums(num1=1, num2=2):
    tot = num1 + num2
    return tot

print(add_2_nums(10, 10))

value1 = add_2_nums(5, 5)
print(value1)

#no arguments supplied, defaults are used
print(add_2_nums())



def hello():
    print("hello world", end="\n")
    # return None if no return is added, return None is the default
   
print(hello())

def favorite_movie():
    movie = input("Whats your favorite movie: ")
    return movie
    
print(favorite_movie())

