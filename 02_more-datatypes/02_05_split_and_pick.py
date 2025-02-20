# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
#
string = input("Enter a string: ")
words = string.split()
word = ""
count = 0

for x in words:
    if words.count(x) > count:
        count = words.count(x)
        word = x

print(f"'{word}' is most common with {count} appearances,")
