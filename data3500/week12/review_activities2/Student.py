class Student:
    def __init__(self, name, major, anumber):
        self.name = name
        self.major = major
        self.__anumber = anumber
        
    def print_student_info(self):
        print("student name: ", self.name)
        print("student major: ", self.major)
        print("student anumber (last four): ", self.__anumber[-4:])
        
    def get_anumber(self):
        return self.__anumber
        
    def set_anumber(self, anumber):
        self.__anumber = anumber
    
andy_student = Student("andy brim", "computer science, finance", "a0012341234")
andy_student.print_student_info()
# print(andy_student.name)
# print(andy_student.major)
# print(andy_student.__anumber)

        
    
        
    