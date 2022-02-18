fil = open("/home/ubuntu/environment/week6/pltr.txt")
lst = fil.readlines()

print(lst)

var = "22.18"
var = float(var)

print(var)

tot = 0
for i in range(len(lst)):
    lst[i] = float(lst[i])
    tot += lst[i]
    
mean = tot / len(lst)

print(mean)

input("press any key")