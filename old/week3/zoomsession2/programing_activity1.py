# write a program that asks the user how old they are,
# and what age they would like to live to.
# calculate how long they have left to live (approximately), and then
# print a friendly message telling the user how long they have to live.

age = int(input("How old are you? "))
desired_age = int(input("How old would you like to live to? "))
life_left = desired_age - age
print("You have", life_left, "years left.  Enjoy your life!!!!")