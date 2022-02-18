sum = 0
for i in range(1,500):
    sum += (1 / 2 ** i)
    print("i, sum: ", i, sum)

# at what iteration does our sum reach .999
# in other words, what iteration do we see .999 twice in a row (iteration 11)
# this is similar to approximating pi - at what iteration do you see 3.14 twice in a row?

def sum4(num1=1, num2=2):
    res = num1 + num2
    return res
    
print(sum4(3,4))
print(sum4(3))
print(sum4())

import random
num1 = random.randint(1,10)
print("num1: ", num1)

import math
print(math.sqrt(16))