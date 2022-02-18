try:
    num1 = 0
    den1 = 5
    print(num1 / den1)
    
    num2 = 5
    den2 = 0
    print(num2 / den2)
    
except:
    print("you tried to divide by zero")
    
print("made it past the try/except")
   
# num2 = 5
# den2 = 0
# print(num2 / den2) 

# print("end of the program")


try:
    pre_path = "/home/ec2-user/environment/week7/zoomsession2/"
    file_path = "GOOG2.txt"
    file = open(pre_path + file_path)
except:
    print("I cant find that file!")