'''
Write a program where the user enters a numeric grade, and receives a message telling them their letter grade.  I.e. >=90 is A, >=80 is B, etc.
Write a Python program to determine if your car needs an emissions test this year
Write a Python program to determine the area of a cuboid, where the user enters values for length, width, and height.
Write a Python program to output a food cart menu to the screen.  The only requirements are it has to be 4 or more items, and must use tabs for alignment
    Food item	Price
    Pizza		$8
    Soda		$1
    Salad		$10
'''

grd = eval(input("What grade are you going to get in this class? "))
if grd >= 90:
    print("You are awesome, you got an A!!!!!!!")
elif grd >= 80:
    print("You got a B, not bad at all!")
elif grd >= 70:
    print("You got a C, that's very interesting!")
elif grd >= 60:
    print("You got a D, you have been having alot of fun outside of this class.  That is fun!")
else:
    print("You get to take this fun class again!!!!")
    
bozo_bucket = eval(input("What is the highest bucket you got to?"))
if bozo_bucket >= 1:
    print("you win a candy bar")
if bozo_bucket >= 2:
    print("you win a card game")
if bozo_bucket >= 3:
    print("you win a toy doll")
if bozo_bucket >= 4:
    print("you win a kite")
if bozo_bucket >=5:
    print("you win a bicycle")
if bozo_bucket >= 6:
    print("you win a 50 dollar bill!!!!")
    