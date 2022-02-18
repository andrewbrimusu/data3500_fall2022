num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

twoD = []
for i in range(num1):
    twoD.append([])

print(twoD)
    
    
for i in range(1, num1+1): #
    for j in range(1, num2+1): # update range
        # print(i,j)
        twoD[i-1].append(i * j)

print(twoD)
    
for i in range(num1):
    for j in range(num2):
        print(twoD[i][j], end=" ")
    print()
        