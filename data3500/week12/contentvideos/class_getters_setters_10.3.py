import numpy as np

class Person():
    def __init__(self, name, age, height, grades):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        
    def calc_avg_grades(self):
        return np.mean(self.grades)
        
    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
        
    def get_height(self):
        return self.height
        
    def get_grades(self):
        return self.grades
        
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
        
    def set_heigh(self, height):
        self.height = height
        
    def set_grades(self, grades):
        self.grades = grades
        
        
        
    
    
p1 = Person("andy", 39, 75, [89, 88, 95])
print(p1)
print(p1.get_name())
print(p1.get_age())
print(p1.get_height())
print(p1.get_grades())
print(p1.calc_avg_grades())

p1.set_grades([100,100,100])
print(p1.calc_avg_grades())


#checkpoint activity
# - Using the class your created in the checkpoing activity for section 10.2
# - add a setter function for birthday_heights.  Or whatever list you added to your class
# - use the setter function to update the list
# - call the find_Max_Height() function (or whatever you named your function)
# - and verify the list has been changed















# solution

class Person():
    def __init__(self, name, age, birthday_heights):
        self.name = name
        self.age = age
        self.birthday_heights = birthday_heights
        
    def get_birthday_heights(self):
        return self.birthday_heights
            
    def set_birthday_heights(self, birthday_heights):
        self.birthday_heights = birthday_heights
        
    def find_Max_Height(self):
        return max(self.birthday_heights)

        
my_object = Person("andy", 39, [24, 30, 34, 37])
print(my_object.find_Max_Height())

my_object.set_birthday_heights([24, 30, 34, 37, 40])
print(my_object.find_Max_Height())
