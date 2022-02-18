print("hi everybody!")

hw_scores = [10, 49.5, 45.0, 50]

print(hw_scores)

tot = 0.0
for h in hw_scores:
    tot += h
    
print("average: ", tot/len(hw_scores))

caleb = [10, 49.5, 45.0, 50]
cale = [10, 48, 47.0, 50]
Hannah = [10, 49.5, 50, 50]

students = [caleb, cale, Hannah]
print("students: ", students)

student_total = 0.0
ct = 0
for student in students:
    tot = 0.0
    for hw_score in student:
        tot += hw_score
        ct += 1
    print("student average: ", tot/len(student))
    student_total += tot
    
print("all students average: ", student_total/ct)

    
lindsay = [10, 48, 49, 50]
mw = [10, 47, 50, 46]
dustin = [10, 50, 48, 47]

class2_students = [lindsay, mw, dustin]

all_classes = [students, class2_students]

all_classes_tot = 0.0
ct = 0
for clas in all_classes:
    for student in clas:
        for hw_score in student:
            all_classes_tot += hw_score
            ct += 1
print("All classes homework average: ", all_classes_tot/ct)



    
    