try:
    open("this file doesnt exist")
except:
    print("this file does not exist")
    
try:
    print(0/5)
    print(5/0)
except:
    print("somebody put a zero in the denominator")
    
    
print("python program is still running")

# checkpoint activity
# 1. have a user enter two integers: a numerator and a denominator
# 2. in a try statement perform division by zero
# 3. in an except statement print a message you divided by zero






























# solution
num = int(input("enter a numerator: "))
den = int(input("enter a denominator: "))

try:
    print(num / den)
except:
    print("you put a zero in the denominator but thats ok")