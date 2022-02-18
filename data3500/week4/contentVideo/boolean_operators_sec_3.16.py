# boolean, True, False
having_a_great_time = True
if having_a_great_time:
    print("awesome!")
    
ready_to_quit = False
if ready_to_quit:
    print("keep going!")
else:
    print("keep up the great work!")
    
# comparison operators
age = 39
old = age > 90
print("old: ", old)

# and 
if having_a_great_time and not ready_to_quit:
    print("awesome, keep up the great work!")
    
    
# or statement
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# or is like addition
# 1 + 1 = 1 # boolean
# 1 + 0 = 1
# 0 + 1 = 1
# 0 + 0 = 0


# and statement
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# # and is like multiplication
# 1 * 1 = 1
# 1 * 0 = 0
# 0 * 1 = 0
# 0 * 0 = 0


age = 39
parent_permission = False # because I dont need permission
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)

age = 12
parent_permission = True
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)

age = 12
parent_permission = False
can_you_fly = age > 14 or (age <= 14 and parent_permission)
print("can_you_fly: ", can_you_fly)

