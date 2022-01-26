import math

print(math.sqrt(25))
print(math.pow(5,2))

print(25 ** 0.5)
print(5 ** 2)


import random

print(random.randint(1,10))

for _ in range(10):
    print(random.randint(1,10))
    
print("-----")

print(random.randrange(10))

for _ in range(10):
    print(random.randrange(1,11))
    
random_nums = []
for _ in range(1000000):
    random_nums.append(random.randint(1,1000))

# print(random_nums)

