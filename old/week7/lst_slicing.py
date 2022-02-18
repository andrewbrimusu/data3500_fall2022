lst = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(lst)
print(lst[0])
print(lst[1])
print(lst[2])

# slice operator uses a range number, meaning it slices
# up to but not including the index 3
lst_a = lst[0:3]

print(lst_a)

#slice starting_index:index_range_number
lst_b = lst[2:6]

print(lst_b)

print(lst[2:]) #c through the end
print(lst[2:8])

# def isPalindrome(s):
#     return s == s[::-1] #racecar
    
print(lst[:4]) # a through d

colors = ["aggie blue", "fighting white", "red"]
for color in colors:
    for character in color:
        print(character)
        
    print(color)