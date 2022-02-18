import numpy
import random

np1 = numpy.zeros(100)
print(np1)

for i in range(len(np1)):
    np1[i] = random.randint(1,100)
    
print(np1)    