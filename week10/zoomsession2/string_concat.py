first_name = "andy"
last_name = "brim"
full_name = first_name + " " + last_name

print("full name: ", full_name)

msg = "hooray "

for i in range(4):
    msg += msg
    print(msg, "---")

print(msg)

msg2 = ""

for i in range(4):
    msg2 += "I love this guy! \n"
print(msg2) 

new_msg = "Go Aggies!"

new_msg = new_msg * 1000000
# print(new_msg)
