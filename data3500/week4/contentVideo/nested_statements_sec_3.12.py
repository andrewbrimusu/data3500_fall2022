# nested statements referes to statements inside of statements
# sentinel_values has if statements inside of while loops

# nested for loops
for row in range(3):
    for col in range (4):
        print(row * col, " ", end="")
    print()