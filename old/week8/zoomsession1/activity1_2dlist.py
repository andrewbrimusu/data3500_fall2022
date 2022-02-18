num1 = int(input("Enter num1: ")) # 2
num2 = int(input("Enter num2: ")) # 3

table = []
for i in range(num1):
    table.append([])
    
print(table)

for i in range(1,num1+1):
    for j in range(1, num2+1):
        table[i-1].append(i*j)
        # print(i*j, end="")
    print()
        
print(table)

for row in table:
    for column in row:
        print(column, end=" ")
    print()