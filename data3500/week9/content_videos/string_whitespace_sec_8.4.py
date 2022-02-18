# strip whitespace
pi = "\t\n\t 3.1415 \t\n\t"
print(pi)

print(pi.strip())
print(pi.rstrip())
print(pi.lstrip())

print(pi)

pi = pi.strip()
print(pi)









# checkpoint activity
# -get a float number from the user, entered as a string
# -remove all the whitespace while the inputted value is still a string
# -convert the string to a float
# -add 10 to the number
# -print the number


num = input("Enter a float with extra whitespace: ")
num = num.strip()
num = float(num)
num += 10
print(num)