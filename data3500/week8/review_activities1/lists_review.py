lst = [[1,2,3], [2,3,4], [3,4,5]]
print(lst[2]) # prints list [3,4,5]
# print(lst[2,2]) # tuple as index error
# print(lst[2[2]]) # index subscript needs to be an int
print(lst[2][2]) # correct, this give me 5
 
threeDList =  [
[[1,2,3], [2,3,4], [3,4,5]],
[[4,5,6], [6,7,8], [7,8,9]],
[[8,9,10], [9,10,11], [10,11,12]]
]

print(threeDList)
print(threeDList[2][2][2])