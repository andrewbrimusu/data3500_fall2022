whitespace_txt = "   \t\t\t\n\n\n\t      hello      \n   "

print(whitespace_txt)

s1 = whitespace_txt.rstrip()
print(s1)

s2 = whitespace_txt.lstrip()
print(s2)

no_whitespace = whitespace_txt.strip()
print(no_whitespace)

sentence = "   I have a dream\n\n\n"
print(sentence)
print(sentence.lstrip())
print(sentence.rstrip())
print(sentence.strip())

