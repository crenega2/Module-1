#Write a script that takes in two strings from the user. If one string is the suffix of the other string, print "True", otherwise, print "False". For example, if the user enters "brush" and "paintbrush", then the script would print "True". If the user entered "painting" and "painted", the script would print "False" because no string ends with the other. Keep in mind that the the pair "brush" and "paintbrush" as well as the pair "paintbrush" and "brush" would print "True" because order does not matter.

word1 = input("Please enter your first word: ")
print("You entered: " + word1)

word2 = input("Please enter your second word: ")
print("You entered: " + word2)

if word2.endswith(word1):
    print("True")
else:
    print("False")