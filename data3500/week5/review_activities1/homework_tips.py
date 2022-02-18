# tip for 3.4
# @@@@@
# @@@@@

for i in range(2):
    for j in range(5):
        print("@", end="")
    print()


####################################################
# tip for 3.9


user_input = 123456
i = 100000000000
while i >= 1:
    if i > user_input:
        print(user_input, "is less than", i)
    else: # this is where you add the logic to floor divide to get the digit, and mod to update user_input
        print(user_input, "is greater than", i)
        print(user_input // i)
        user_input = user_input % i
    i /= 10




# tip for 3.12
num1 = 54145
dig1 = num1 // 10000
dig2 = num1 % 10

print("num1, dig1, dig2: ", num1, "\n", dig1, dig2)

# chopping off the first digit and fifth digit
num1 = num1 % 10000
print("num1: ", num1)

num1 = num1 // 10
print("num1: ", num1)



for i in range(10):
    print(i)# this prints 0 to 9
print()
for i in range(9,-1,-1): # this prints 9 to 0
    print(i)
    
print("___________________________")
print("palindrome example")

user_input = input("Enter a number: ")
user_len = len(user_input)
print("user_len: ", user_len)

#dont do this on the homework
for i in user_input:
    print(i)
    
# print(user_input[0])
# print(user_input[1])
# print(user_input[2])
# print(user_input[3])

# print(user_input[3])
# print(user_input[2])
# print(user_input[1])
# print(user_input[0])

palindrome = ""
for i in range(len(user_input)-1, -1, -1): # start is one less than number of characters, range is -1, step is -1
    palindrome += user_input[i] # string concatenation

print("palindrome: ", palindrome)


print("Example of printing each character in a string")
name = "andyb"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


print("------------------approximating pi---------------")
numerator = 4
i = 1
pi = 0
sum = 0
for denominator in range(1,6000,2):
    if i % 2 == 1:
        sum += numerator / denominator
    else:
        sum -= numerator / denominator
    #print("i: ", i, sum)
    i += 1
    
print ('bob' == 'bob'[::-1])


user_input = 1234567891
i = 100000000000
print(user_input)
while i >= 1:
    if user_input >= i:
        print(int(user_input // i))
        user_input = user_input % i
    i /= 10
