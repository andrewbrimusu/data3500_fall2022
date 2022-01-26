gmat = 740
gpa = 3.5
seems_decent = True

great_gmat = gmat >= 750
good_gpa = gpa >= 3.5
average_criteria = (gmat >= 650) and (gpa >= 2.8)

if great_gmat or good_gpa: 
    print("Welcome to Huntsman Grad School!!!!!!!!")
elif average_criteria:
    print("Welcome to Huntsman, you barely made it!")
else:
    print("Sorry, you should got to Bridgerland, the Cornell of Cache Valley")


    