# Activity 1 - Write a program that prints all the multiples of 5, 
# from 5 to 95.  Start your loop at 5.

start = 5
range_num = 96 # one greater than 95
step = 5
for i in range(start, range_num, step):
    print(i, end=" ")
print()
print("i: ", i)


for i in range(10):
    print(i)