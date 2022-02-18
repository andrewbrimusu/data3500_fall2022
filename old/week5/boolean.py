gmat = 740
gpa = 3.5
seems_decent = True

great_gmat = gmat >= 750
good_gpa = gpa >= 3.5
average_criteria = (gmat >= 650) and (gpa >= 2.8)

print(great_gmat, good_gpa, average_criteria)


if great_gmat or good_gpa: 
    print("Welcome to Huntsman Grad School!!!!!!!!")
elif average_criteria:
    print("Welcome to Huntsman, you barely made it!")
else:
    print("Sorry, you should got to Bridgerland, the Cornell of Cache Valley")
    
    
print(True and True) # 1 x 1
print(True and False) # 1 x 0
print(False and True) # 0 x 1
print(False and False) # 0 x 0

print(True or True)
print(True or False)
print(False or True)
print(False or False)







    