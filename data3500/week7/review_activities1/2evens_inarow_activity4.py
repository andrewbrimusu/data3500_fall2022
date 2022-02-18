
import random
lst = []

for i in range(10):
    lst.append(random.randint(1, 100))
    
print("lst: ", lst)
    
print("----------------------------------")
i = 0
for l in lst:
    # print(l)
    if i > 0:
        print(lst[i]) # l and lst[i] are the same value, each time
        print(lst[i-1])
        
        # check for lst[i] and list[i-1] both even
        if lst[i] % 2 == 0 and lst[i-1] % 2 == 0:
            print("both",lst[i],"and",lst[i-1],"are even")
    
    print("----------")
    i += 1
    
    
    
    
# lst[count] and lst[count+1]
# lst[count:count+2]
# separate variables


