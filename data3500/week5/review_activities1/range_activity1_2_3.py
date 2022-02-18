# 1. Write a loop that goes down from 20 to 2, counting down by 2 each time.  So the output should be...
# 20 18 16 14 12 10 8 6 4 2
print("hows it going?")
for i in range(20, 1, -2):
    print(i, end=" ")
    
print()

# 2. Modify the loop in activity 1, to go down to 10, and then break the loop.  So the output should be...
# 20 18 16 14 12 10
for i in range(20, 1, -2):
    print(i, end=" ")
    if i == 10:
        break
print()

# 3. Modify the loop in activity 1, to go down to 10 and skip 10, but keep going with 8, all the way down to 2.  So the output should be...
# 20 18 16 14 12 8 6 4 2
for i in range(20, 1, -2):
    print(i, end=" ")
    
print()
user_input = 123456
i = 10000000
while i >= 1:
    if i > user_input:
        print(user_input, "is less than", i)
    else:
        print(user_input, "is greater than", i)
    i /= 10

