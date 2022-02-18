age = 39
age = age + 1
print("age: ", age)
age += 1
print("age: ", age)

age -= 1
print("age: ", age)

age /= 2 # float division
print("age: ", age)


if age == 20:
    print("20 is great!")
    if age == 20:
        print("20 is great!")
        if age == 20:
            print("20 is great!")
            if age == 20:
                print("20 is great!")
                
itr = 0
for i in range(10):
    for j in range(100):
        print("i,j, itr: ", i, j, itr)
        itr += 1
       
# the break statement will only terminate a loop, one level deep.
# It will not terminate nested loops.
print("\n\n\n")
itr = 0
for i in range(3):
    for j in range(10):
        if j == 8:
            break
        print("i,j, itr: ", i, j, itr)
        itr += 1     