twod_list = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16,17,18,19]]

print("twod_list: ", twod_list)

print(twod_list[1])
print(twod_list[1][3]) # prints the 8

for i in range(len(twod_list)):
    for j in range(len(twod_list[i])):
        print(twod_list[i][j])
        
print(twod_list[3][6] - twod_list[2][2]) # 19 - 11

threed_list = [[[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16,17,18,19]],
[[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16,17,18,19]]]

        
        