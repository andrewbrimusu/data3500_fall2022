sentence = "dude, I just biked down that mountain \
and at first I was like Whoa and then I was like Whoa"
sentence = sentence.capitalize()
print(sentence)
words = sentence.split()

first_whoa = True
i = 0
for word in words:
    if word[:4] == "whoa" and first_whoa:
        words[i] = words[i].lower()
        first_whoa = False
    elif word[:4] == "whoa" and not first_whoa:
        words[i] = words[i].upper()
    else:
        pass
    i += 1
    
new_sentence = ""
for word in words:
    new_sentence += " " + word
    
new_sentence += "!"

print(new_sentence)
    
