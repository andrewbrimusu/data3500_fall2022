file = open("/home/ec2-user/environment/week11/zoomsession1/example.txt", "w")
file.write("hello\n")
file.write("world\n")
# file.close() # without closing the file, it cant be reopened on line 11


with open("/home/ec2-user/environment/week11/zoomsession1/example2.txt", "w") as file2:
    file2.write("hello again\n")
    file2.write("world again\n")
    
file3 = open("/home/ec2-user/environment/week11/zoomsession1/example.txt")
print(file3.readlines())

file4 = open("/home/ec2-user/environment/week11/zoomsession1/example2.txt")
print(file4.readlines())

import os
os.system("ls")
if os.path.exists("/home/ec2-user/environment/week11/zoomsession1/example.txt"):
    os.system("rm " + "/home/ec2-user/environment/week11/zoomsession1/example.txt")

    