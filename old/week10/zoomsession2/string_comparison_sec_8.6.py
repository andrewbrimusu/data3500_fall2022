# string comparison

if "andy " == "Andy":
    print("they are the same")
else:
    print("they are different")
    
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))

print("andy" == "andy")
print("andy" == "brim")
print("brim" == "Brim")
print(65 == ord("A"))



# checkpoint activity
# -have the user enter two strings
# -print to the console whether they are same value

























# solution
str1 = input("enter a string: ")
str2 = input("enter another string: ")
if str1 == str2:
    print("They are the same value")
else:
    print("They are not the same value")