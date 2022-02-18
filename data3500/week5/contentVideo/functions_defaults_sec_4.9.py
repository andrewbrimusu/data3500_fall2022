# function definition
def biggest(arg1=0, arg2=0, arg3=0, arg4=0):
    num = max(arg1, arg2, arg3, arg4)
    return num
    
# function call
res1 = biggest(2,4,6,8)
print(res1)

res2 = biggest(-1,-2,-3,-4)
print(res2)

res3 = biggest()
print(res3)

res4 = biggest(10)
print(res4)

res5 = biggest(-10, -5)
print(res5)

res6 = biggest(-10, -5, 100)
print(res6)