#Write a script that takes in a string from the user. Print the string where all the lower case letters are shifted to the front and the spaces removed. Keep the relative order of the lower case letters and upper case letters.

input = input("Enter a string: ")
lowercase = ''.join([char for char in input if char.islower()])
uppercase = ''.join([char for char in input if char.isupper()])
updated = lowercase + uppercase
print("Updated:", updated)