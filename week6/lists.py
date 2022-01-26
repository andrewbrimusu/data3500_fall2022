lst = [3, 1, 4, 1, 5, 9, 2, 6]

# lists allow hetergenous data
# but good style uses homogenous data in lists (same type)
# lst = ["andy", "is", 40] # hetergenous data, or mixed types

print(lst)

#example of a for loop
for i in range(2):
    print(i)
    
print("----")

for item in lst:
    print(item)
    
#adding items to a list using the append function()

lst.append(5)
lst.append(9)
lst.append(2)

for item in lst:
    print(item)
    
print("-----")

print(lst[0]) # first item in the lst
print(lst[1]) # second item in the lst
print(lst[2]) # third item in the lst

lst[0] = 1000 # changing first item in the lst

print(lst[0])

print("-----")

lst[0] = 3
print(lst[0])

# print(lst[0:3]) # slicing, covered in a later lecture

# print items in list using the index operator
for i in range(len(lst)):
    print(lst[i])
    
    





