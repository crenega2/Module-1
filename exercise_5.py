#Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. Create a third array containing the common values from both arrays without duplicates. Print out all three lists.

print("For list 1, please enter 5 numbers")
Array1 = []
for x in range(5):
    Array1.append(int(input(f"Please enter number {x+1}: ")))

print("For list 2, please enter 5 numbers")
Array2 = []
for x in range(5):
    Array2.append(int(input(f"Please enter number {x+1}: ")))

Array3 = []
for i in range(5):
    if Array1[0] == Array2[i]:
        Array3.append(Array2[i])
for i in range(5):
    if Array1[1] == Array2[i]:
        Array3.append(Array2[i])
for i in range(5):
    if Array1[2] == Array2[i]:
        Array3.append(Array2[i])
for i in range(5):
    if Array1[3] == Array2[i]:
        Array3.append(Array2[i])
for i in range(5):
    if Array1[4] == Array2[i]:
        Array3.append(Array2[i])

#Using set will automatically get rid of all repeat numbers
Array3 = list(set(Array3))

print(f"Your first list: {Array1}")
print(f"Your second list: {Array2}")
print(f"Your third list: {Array3}")
