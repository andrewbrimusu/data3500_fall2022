# replace() function
phrase = "This class is ok"
print("phrase: ", phrase)

phrase = phrase.replace("ok", "amazing!!!!")
print("phrase: ", phrase)


# checkpoint activity
# start with a string which states your favorite fruit
# for example mine would be: "my favorite fruit is an apple"
# Then contatenate, to the beginning of the string, "Nevermind, "
# Using the replace function, replace your first favorite fruit with your second favorite fruit
# Print the new string to the console

















# solution
phrase = "my favorite fruit is an apple"
phrase = "Nevermind, " + phrase
phrase = phrase.replace("apple", "orange")
print(phrase)


