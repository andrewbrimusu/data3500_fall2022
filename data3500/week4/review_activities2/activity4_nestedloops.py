print("\t1\t2\t3\t4\t5")
print("-----------------------------------------")
for i in range(5):
    print(i+1,end="|")
    for j in range(5):
        print("\t"+str((j+1)*(i+1)),end="")
    print()
    
    