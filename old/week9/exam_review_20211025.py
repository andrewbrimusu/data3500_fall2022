import math


# true or false, these are valid python variables:
having_fun1 = True
havingFun1 = True
# 1havingFun = False # not valid

waebvyduaweyauiwbvuyaieguaweighaweugiab = 100
# bad confusing name
# name variables what they are and
# name functions what they do

# typing
name = "andy"
print(name)
print(id(name))
name = "brim"
print(id(name))
name = "andy"
print(id(name))

name = 38
# dynamic typed, type can be changed while running the program

# static = fixed not changeable
# dynamic = changeable



# operators 

print(5 / 2)
print(5 // 2)

#negatives, the floor function will "round down"
print(-5 // 2) # -3
# to "round up" a negative use the math.ceil function
print(math.ceil(-5 / 2)) # -2

print(9 / 3)


# range function returns a list up to one less in magnitude,
# for example a range(5) returns 0 through 4, not including 5

print("*******")
for i in range(5):
    print(i)
    
# same range as above
print("-----")
for i in range(0,5):
    print(i)
    
print("-----")
for i in range(0,-5,-1):
    print(i)

prices = [2,3,2,3,3,4,5,4,3,2,3,2]
for p in prices:
    print("p: ", p)
    
    

# rounds down
print(-5 // 2) # -3
print(5 // 2) # 2

print("andy" + "brim")
print("twenty" + "20")

age = 39

if age > 30:
    print("you are old")
    
print(3 == 5)

# while age > 30:
#     print("you are old") # logic error, needs something to end the loop
    
age = 0
while age <= 40:
    print(age)
    age += 1
    
    
for i in range(1,6):
    print(i, ",", sep="", end=" ")
    
print("@@@@@@@@@")

# this loop prints ct, 20 times.
# 10 i iterations * 2 j iterations
# j loop breaks after 2 iterations, when j == 1
ct = 0
for i in range(10):
    for j in range(3):
        print("ct: ", ct, end=" ")
        ct += 1
        if j == 1:
            break
    print()

print("----- separate argument -----")
print(1,2,3,4,5,sep=",")
    
print("----- end argument -----")
print(1,2,3,4,5,end=",")

print("\n------")
print(print(2))

# default for sep argument is: space
# default for end argument is: newline (or return)
print()

# function definition
# 4 parts to a function: name, parameter list, logic, return statement
# 1. name
# 2. parameter list 
# 3. logic
# 4. return statement
def sum(one, two, three): # name and parameter list
    tot = one + two + three # logic
    return tot # return statement
    
# function call
# 1. function name
# 2. function arguments
print("sum function returns: ", sum(2, 4, 6))

lst = [1,2,3,4,5]
print(lst[1:4])



# palindrome in Python

string = "racecar"
if string == string[::-1]:
    print("palindrome")
    
def isPalindrome(strn):
    return strn == strn[::-1]
    
print(isPalindrome("racecar"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("ilovethisguy"))
print(isPalindrome("ratsliveonnoevilstar"))


lst = [1,2,3,4,5]
print(lst[1:4]) # start idx 1, end idx 3

print(lst[-1:-4:-1]) # 5 4 3

print(lst[4:0:-1])

print(lst[2::-1]) # print 3, 2, 1

favorite_words = ["fransisco", "camey"]

# printing each character in a list of words
for word in favorite_words:
    for letter in word:
        print(letter, end="")
        
    print()
