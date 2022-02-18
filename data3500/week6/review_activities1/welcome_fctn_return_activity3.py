def welcome_fctn(name, age, favorite_color):
    welcome_message = "Welcome " + name + \
    ", you are " + str(age) + " years old, and " + \
    favorite_color + " is your favorite color."
    
    return welcome_message
    
print(welcome_fctn("andy", 39, "aggie blue"))
var1 = welcome_fctn("andy brim", 39, "fighting white")
print("var1: ", var1)