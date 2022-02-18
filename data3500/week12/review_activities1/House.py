house = {}
house["sqft"] = 3000
house["totrooms"] = 8
house["bedrooms"] = 4
house["bathrooms"] = 3
house["hasMstrCloset"] = True
house["acreage"] = 3
house["location_city"] = "Logan"


class House:
    def __init__(self, sqft, totrooms, bedrooms, bathrooms, hasMstrCloset, acreage, location_city):
        self.sqft = sqft
        self.totrooms = totrooms
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.hasMstrCloset = hasMstrCloset
        self.acreage = acreage
        self.location_city = location_city
        
    def calcValue(self):
        return self.sqft * 110
        
    def __str__(self):
        return "square footage: " + str(self.sqft)
        
my_house = House(3000, 8, 4, 3, True, 3, "Logan")

print(my_house.sqft)
print(my_house.calcValue())
print(str(my_house))

my_other_house = House(5000, 10, 6, 4, True, 10, "Hyde Park")
print(my_other_house.location_city)
print(my_other_house.calcValue())




