import math
import numpy


a = [[77, 68, 86, 73], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]] # third student's grades
     
# print 90
print(a[2])
print(type(a[2]))


print(a[2][1])
print(type(a[2][1]))

print("-------")
for item in a:
    print(item)
    for item2 in item:
        print(item2)
        
    
brim = [[[77, 68, 86, 73], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]],
     
     [[77, 68, 86, 73], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]]]
     
     # third student's grades
         
for a in brim:
    for b in a:
        for c in b:
            print(c)
            
# Izzy is a genius
# try this code, and say I'm wrong
# print("--------#")
# a_ctr = 0
# for item in brim:
#     for item2 in brim[a_ctr]:
#         print(item2)
#     a_ctr += 1
            
            
            
# four dimensional list
# jagged list - all lists are not the same size
# jagged lists are ok, since naturally some data has different sizes
fourd = [[[[77, 68, 86, 73], # first student's grades
     [96, 87, 89], # second student's grades
     [70, 90, 86, 81]],
     
     [[77, 68, 86, 73], # first student's grades
     [99, 87, 89, 81], # second student's grades
     [65, 90]]],
     
     [[[77, 68, 86, 73], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]],
     
     [[77], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]]]]
            
# avg = sum(fourd) / len(fourd)
# print("avg: ", avg)

tot = 0
num_items = 0
max = -999999
min = 999999
print("////////")
for a in fourd:
    for b in a:
        for c in b:
            for d in c:
                tot += d
                num_items += 1
                if d > max:
                    max = d
                if d < min:
                    min = d
                
                
avg = tot / num_items
print("avg: ", avg)

print("max: ", max)
print("min: ", min)


new_list = []
for a in fourd:
    for b in a:
        for c in b:
            for d in c:
                new_list.append(d)
            
print(new_list)
print("avg: ", sum(new_list) / len(new_list))
print("max: ", numpy.max(new_list))
print("min: ", numpy.min(new_list))





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
                




