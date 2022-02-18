for i in range(5,96,5):
    if i > 85: # terminating the loop when i is greater than 85
        break
    print("i: ", i)
    
print("\n\n\n")  
for i in range(5,96,5):
    k = 100
    if i == 85: #skipping the rest of the loop (not printing) when i is 85
        continue
print("i: ", i)
print("k: ", k)