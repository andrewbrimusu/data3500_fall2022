# function definition
def biggest(arg1=0, arg2=0, arg3=0, arg4=0):
    num = max(arg1, arg2, arg3, arg4)
    return num
    
# function call
res1 = biggest(2,4,6,8)
print(res1)

res2 = biggest(-1,-2,-3,-4)
print(res2)