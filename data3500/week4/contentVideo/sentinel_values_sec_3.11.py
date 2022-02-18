# program that executes a while loop with a sentinel
selection = 0
while selection != 5:
    print("Welcome to the happy message program!")
    print("Enter one of the following selections...")
    print("1. Show the weather")
    print("2. How's my day going to go?")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        print("The weather is beautiful!\n")
    if selection == 2:
        print("Your day will be amazing!\n")
    if selection == 5:
        print("Thanks for coming!\n")
    