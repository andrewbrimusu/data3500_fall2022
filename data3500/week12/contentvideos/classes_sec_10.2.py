import numpy as np

person_dct = {}
person_dct["name"] = "andy"
person_dct["age"] = 39
person_dct["height"] = 75
person_dct["grades"] = [85, 89, 93]

def avg_grades(grades):
    return np.mean(grades)

print(avg_grades(person_dct["grades"]))





print("person_dct: ", person_dct)


class Person():
    def __init__(self, name, age, height, grades):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        
    def calc_avg_grades(self):
        return np.mean(self.grades)
    
    
p1 = Person("andy", 39, 75, [89, 88, 95])
print(p1)
print(p1.name)
print(p1.age)
print(p1.height)
print(p1.grades)
print(p1.calc_avg_grades())




# checkpoing activity
# - write your own Person class and add a new list data type of your own
# - have the list contain numbers.  it could be your height on your first 4 birthdays
# - add a function to your class to find_Max_Height() which returns the highest value in the list
# - create an object with the class called "my_object", and pass in the appropriate values to the constructor
# - call the function to find_Max_Height() on your object and print the result





















# solution

class Person():
    def __init__(self, name, age, birthday_heights):
        self.name = name
        self.age = age
        self.birthday_heights = birthday_heights
        
    def find_Max_Height(self):
        return max(self.birthday_heights)

        
my_object = Person("andy", 39, [24, 30, 34, 37])
print(my_object.find_Max_Height())

    