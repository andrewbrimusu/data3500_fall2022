galused = 0
milage = 0
milpgal = 0
totalmpg = 0
while galused !=-1:
    galused= int(input("enter the gallons used (-1 to end): "))
    milage= int(input("enter the miles driven: "))
    milpgal= print("the miles per gallon: ", (milage/galused))
    totalmpg= int(sum(galused)/sum(milage))
if galused ==-1:
    print("total miles per gallon: ", totalmpg)