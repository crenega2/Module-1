#Take in 5 words from the user and store them in a list. Then, create a single string from the individual words, separated by spaces, and print the list and resultant string.

words = []
for x in range(5):
    word = input(f"Please enter word {x+1}: ")
    words.append(word)

result = ' '.join(words)
print(f"The list of words: {words}")
print(f"The resultant string: {result}")