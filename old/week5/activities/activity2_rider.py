age = eval(input("Enter your child's age: "))
weight = eval(input("Enger your child's weight: "))

if age >= 12:
    print("Your child may ride in the front seat")
elif age == 11 and weight > 90:
    print("Your child may ride in the front seat")
elif age < 11 and weight > 100:
    print("Your child may ride in the front seat")
else:
    print("Your child may not ride in the front seat")
    
# same exercise, but now using boolean variables
age = eval(input("Enter your child's age: "))
weight = eval(input("Enger your child's weight: "))

criteria_12 = age >= 12
criteria_11 = age == 11 and weight > 90
criteria_younger = age < 11 and weight > 100
can_ride = False

if criteria_12:
    can_ride = True
elif criteria_11:
    can_ride = True
elif criteria_younger:
    can_ride = True
else:
    can_ride = False
    
if can_ride:
    print("Your child may ride in the front seat")
else:
    print("Your child may not ride in the front seat")
    
    