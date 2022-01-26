lst = []

for item in range(2, 101, 2):
    lst.append(item)
    
print(lst)

lst2 = [i for i in range(2, 101, 2)]

# for item in lst2:
#     print(item)
    
eights = []
for i in range(9):
    eights.append(i * 0.125)
    
print(eights)


eights_again = [i * 0.125 for i in range(9)]
print(eights_again)
