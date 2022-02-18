# rounds down
print(-5 // 2) # -3
print(5 // 2) # 2

print("andy" + "brim")
print("twenty" + "20")

age = 39

if age > 30:
    print("you are old")
    
# while age > 30:
#     print("you are old") # logic error, needs something to end the loop
    
for i in range(1,6):
    print(i, ",", sep="", end=" ")
    
print()
print(1,2,3,4,5,sep=",")
    
# 4 parts to a function: name, parameter list, logic, return statement
def sum(one, two, three): # name and parameter list
    tot = one + two + three # logic
    return tot # return statement
    
# palindrome in Python

string = "racecar"
if string == string[::-1]:
    print("palindrome")
    
def isPalindrome(strn):
    return strn == strn[::-1]
    
print(isPalindrome("racecar"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("ilovethisguy"))


lst = [1,2,3,4,5]
print(lst[1:4]) # start idx 1, end idx 3

thisdict = {}
thisdict["brand"] = "Ford"
thisdict["model"] = "Mustang"
thisdict["year"] = 1964
thisdict["color"] = "red"

thisdict.append(5)
     