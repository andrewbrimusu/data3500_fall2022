# Adding values to a list with a for loop
lst = []
for i in range(100):
    lst.append(i)
    
print("lst: ", lst)

# list comprehension
lst = [i for i in range(50)]
print("lst: ", lst)

# updating each value in a list comprehension
lst = [str(i) for i in range(25)]
print("lst: ", lst)

# list comprehension example
file = open("/home/ec2-user/environment/week10/content_videos/AAPL.txt")
lines = file.readlines()
print("lines: ", lines)
prices = [float(line) for line in lines]
print("prices: ", prices)

# checkpoint 
# create a list of even numbers 2 through 100 using a list comprehension













# solution
evens = [i for i in range(2,101,2)]
print("evens: ", evens)