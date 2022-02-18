res1 = 2 ** 2
res2 = 2 ** 3
res3 = 2 ** 4
print(res1, res2, res3)


#function definition
def square(arg1, arg2):
    num = arg1 ** arg2
    return num
    
#function call
res1 = square(2, 2)
res2 = square(2, 3)
res3 = square(2, 4)
print(res1, res2, res3)

for i in range(1, 1000001):
    print(square(i, 2))