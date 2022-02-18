import numpy
import random

# create a list of 4 floats
homework_scores = [49.5, 48.3, 47.6, 50]
print(homework_scores)

# convert the list to a numpy array
hw_np = numpy.array(homework_scores)
print(hw_np)




















# checkpoint activity
# create a list of 10 random numbers
# convert the list to a numpy array







# solution
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print("lst: ", lst)


np1 = numpy.array(lst)
print("np1: ", np1)