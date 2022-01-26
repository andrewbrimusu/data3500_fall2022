# write a program that gets a user's score in this class,
# as a percentage i.e. 90 or 95.
# write an if statement that checks to see if their score is 
# equal to or greater than 93.  If so, print "Congratulations you got an A"
# else print "Congratulations, you still learned a ton!!!!"

score = float(input("Enter your score in this class: "))
if score >= 93.0:
    print("Congratulations, you got an A!!!!")
else:
    print("Congratulations, you still learned a ton!!!!")