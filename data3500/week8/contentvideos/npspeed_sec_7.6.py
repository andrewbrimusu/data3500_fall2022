import numpy
import random
import time

start = time.time()
randoms = []
for i in range(1000000):
    randoms.append(random.randint(1,50))
end = time.time()
#print(randoms)
print("time lapsed: ", end - start)

start2 = time.time()
rands = numpy.random.randint(50, size=1000000)
end2 = time.time()
#print(rands)
print("array time lapsed: ", end2 - start2)


np1 = numpy.zeros(100)
np1 = numpy.random.randint(10, size=100)
print("np1: ", np1)






























# checkpoint activity
# There is no checkpoint activity for this
# content video.
# This is just an exercise to show you how
# powerful numpy arrays can be.