# create a list of even numbers, using the append function
lst = []
for i in range(10):
    lst.append(i * 2)
print("lst: ", lst)



# checkpoint activity
# create a list of 10 random numbers using a for loop, randint, and append functions
# meaning start with an empty list, then loop 10 times, adding a random number each time
import random
lst = []
for i in range(10):
    lst.append(random.randint(1,10))
    
print("lst: ", lst)