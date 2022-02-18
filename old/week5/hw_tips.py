num = 1234567890
i = 10 ** 7
print(num, i)

print(num // i)
print(num % i)

num = num % i
i = 10 ** 6

print(num // i)
print(num % i)


num = num % i
i = 10 ** 5 

print(num // i)
print(num % i)

num = num % i
i = 10 ** 4

print(num // i)
print(num % i)


for i in range(10, 0, -1):
    print(i)

tot = 0
m = 1
for i in range(1, 1000000, 2):
    tot += (4 / (2 * i)) * m
    
    print(tot, i)
    
input("press enter")

