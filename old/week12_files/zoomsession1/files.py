file = open("/home/ubuntu/environment/week12_files/zoomsession1/example.txt", "w")
file.write("hello world\n")
file.write("goodbye world\n")

file.close() # without closing the file, it cant be reopened on line 11

    
file3 = open("/home/ubuntu/environment/week12_files/zoomsession1/example.txt")
print(file3.readlines())




with open("/home/ubuntu/environment/week12_files/zoomsession1/example2.txt", "w") as file2:
    file2.write("hello again\n")
    file2.write("world again\n")

print("hi")


file4 = open("/home/ubuntu/environment/week12_files/zoomsession1/example2.txt")
print(file4.readlines())

import os
os.system("ls")
os.system("pwd")
fil = "/home/ubuntu/environment/week12_files/zoomsession1/example2.txt"
if os.path.exists(fil):
    input("press enter to continue...")
    os.system("rm " + fil)

    