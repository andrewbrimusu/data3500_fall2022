# string.count() function
phrase = "to be or not to be that is the question"

ct = phrase.count("to")
print("ct: ", ct)

ct = phrase.count("to", 1)
print("ct: ", ct)

ct = phrase.count("to", 13)
print("ct: ", ct)

# string.index() function
idx = phrase.index("to")
print("idx: ", idx)

idx = phrase.index("to", 10)
print("idx: ", idx)

# string.rindex() function
idx = phrase.rindex("to")
print("idx: ", idx)



# checkpoint activity
# create a variable that contains the string "row row row your boat"
# use the count() function to determine how many instances of "row" are in the string
# use the index() function to find the index of the first "row"
# use the rindex() function to find the index of the last "row"






















# solution

lyrics = "row row row your boat"
print(lyrics.count("row"))
print(lyrics.index("row"))
print(lyrics.rindex("row"))
