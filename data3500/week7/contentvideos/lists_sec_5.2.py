#lists
ages = [39, 20, 21, 24, 25]

favorite_colors = ["aggie blue", "fighting white", "navy", "red"]

print(ages)

print(ages[0])
print(ages[1])
print(ages[2])
print(ages[3])
print(ages[4])

name = "andy brim"

for letter in name:
    print("letter: ", letter)
    
print(name[0]) # prints a


for i in range(len(name)):
    print(name[i])
    
for color in favorite_colors:
    print(color)
    
print(favorite_colors[1][9]) 


favorite_colors = ["aggie blue", "fighting white", \
    "navy", "red"]
    
for color in favorite_colors:
    print(color)


ages = [40, 27, 21, 22, 25, 42, 20, 21, 19]

total = 0
ct = 0
for age in ages:
    total += age
    ct += 1
avg = total / ct
print(total)
print(ct)
print(avg)


    