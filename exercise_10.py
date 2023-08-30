#Take in a string from the user and split it into an array of single characters. Split the list of characters into a list of lists where each inner list has 3 elements. Notice that the last inner array may have less than 3 elements.

string = input("Please enter a string: ")
characters = list(string)

result = [characters[x:x+3] 
for x in range(0, len(characters), 3)]
print(f"The list of characters: {characters}")
print(f"The list of lists: {result}")