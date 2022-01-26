try:
    fil = open("this_File_doesnt_exist.txt")
except:
    print("you tried to open a file that doest exist.  Program will now continue")
    
# attempting to open file that doest exist
# not in a try block, will crash your program
# inside a try block, it will keep running
# open("file_doesnt_exist.txt")
  
    
    
numerator = 5
denominator = 0

try:
    print(numerator / denominator)
except:
    print("denominator is: ", denominator)
    
    
print("program is ending")  