class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def calcArea(self):
        return self.height * self.width
        
my_rectangle = Rectangle(3,5)
print(my_rectangle.calcArea())