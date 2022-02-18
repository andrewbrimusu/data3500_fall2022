class Person():
    def __init__(self, name, age, height, grades, ssn):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        self.__ssn = ssn
        
    def get_ssn(self):
        return self.__ssn
        
    def set_ssn(self, ssn):
        self.__ssn = ssn
        
    def calc_avg_grades(self):
        return np.mean(self.grades)
        
p1 = Person("andy", 39, 75, [89, 88, 95], 12341234)
print(p1)
print(p1.name)

p1.set_ssn(123412345)
print(p1.get_ssn())

print(p1.name)
# print(p1.__ssn)



# checkpoint activity
# - create a class called Student
# - have the student contain two pieces of data, both strings: name and anumber
# - make name public and anumber private
# - add getter and setter functions for both name and anumber
# - demonstrate that anumber cannot be directly accessed, but must be accessed with a getter function













# solution
class Student():
    def __init__(self, name, anumber):
        self.name = name
        self.__anumber = anumber
        
    def get_name(self):
        return self.name
        
    def get_anumber(self):
        return self.anumber
        
    def set_name(self, name):
        self.name = name
        
    def set_anumber(self, anumber):
        self.anumber = anumber
        
stud1 = Student("andy", "a001234")

print("--------------")
print(stud1.name)
print(stud1.get_name())

print("--------------")
print(stud1.get_anumber())
print(stud1.__anumber)
