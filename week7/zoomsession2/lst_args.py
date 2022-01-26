def sum_lst(lst):
    tot = 0.0
    for num in lst:
        tot += num
        
    lst.append(5)
    lst.append(9)
    lst.append(2)
        
    return tot
    

lst = [3,1,4,1]
print("id: ", id(lst))
lst2 = lst



print(sum_lst(lst))
print("id: ", id(lst))

print(lst)
print(lst2)



age = 40

def birthday(age):
    print("id: ", id(age))
    age += 1
    print("id: ", id(age))
    print("new age: ", age)
    new_age = 42
    print(id(new_age))
birthday(age)

print("age back in main: ", age)
print("id: ", id(age))

new_val = 41
print("id: ", id(new_val))

new_age2 = 42
print(id(new_age2))

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

print(lst.index(3))
print(lst.index(2))






