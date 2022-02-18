'''
Activity 2 - While loop: Write a program that asks a user to type in their homework grades (as many as they want), 
in a while loop.  Keep a running total of their homework score, and how many grades they entered.  Quit the loop when they enter "-1" and print their average homework score.
'''
tot = 0
grades_entered = 0
user_grd = ""

while user_grd != "-1":
    user_grd = input("Enter your grade, -1 to quit: ")
    if user_grd == "-1":
        break
    tot = tot + float(user_grd)
    grades_entered = grades_entered + 1
    
print("Average grade: ", tot / grades_entered)