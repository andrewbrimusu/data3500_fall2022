class Cube:
    def __init__(self, length):
        self.length = length
        
    def calc_volume(self):
        return self.length ** 3
        
    def calc_surface_area(self):
        return self.length ** 2  *6
        
        
cube1 = Cube(3)
print(cube1.calc_surface_area())
print(cube1.calc_volume())

