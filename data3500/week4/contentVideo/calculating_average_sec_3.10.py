#grades
grades = [50.0, 45.0, 48.0, 10.0]

#adding grades
tot = 0.0
num_grades = 0
for grad in grades:
    tot += grad
    num_grades += 1

#finding average
avg = tot / num_grades
print("average grade is: ", avg)

