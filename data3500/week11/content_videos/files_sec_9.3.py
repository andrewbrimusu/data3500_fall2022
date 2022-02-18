# open and write to file1
file1 = open("output1.txt", "w")
file1.write("hello\n")
file1.write("goodbye\n")

# open and write to file using "with"
with open("output2.txt", "w") as file2:
    file2.write("hello again\n")
    file2.write("goodbye again\n")
    
# reopen and read from file1
file1_again = open("output1.txt", "r")
print(file1_again.readlines())

# reopen and read from file2
file2_again = open("output2.txt", "r")
print(file2_again.readlines())





#checkpoint activity
# 1. open a file for writing called favorite_colors.txt
# 2. write your three favorite colors as strings to the file
# 
# 3. open a file using the with command, called favorite_songs.txt
# 4. write your 3 favorite songs as strings to the file























# solution
f1 = open("favorite_colors.txt", "w")
f1.write("blue\n")
f1.write("white\n")
f1.write("red\n")

with open("favorite_songs.txt", "w") as f2:
    f2.write("Don't stop believing\n")
    f2.write("Dream on\n")
    f2.write("I barely knew you\n")