import random

user_dice = random.randint(1,6)
computer_dice = random.randint(1,6)
print("User dice: ", user_dice)
print("Computer dice: ", computer_dice)

if user_dice > computer_dice:
    print("User wins!")
else:
    print("Computer wins!")