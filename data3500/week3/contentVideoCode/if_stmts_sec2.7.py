# if stmt
if 5 > 10: #False
    print("5 is greater")

if 10 > 5: #True
    print("10 is greater")
    
print(10 < 5)
print(10 > 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

age = 39

your_age = eval(input("Enter your age: "))
if your_age < age:
    print("You are younger than Andy")
    
if age < your_age:
    print("You are older than Andy")