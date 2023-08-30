#Take in a number, n, from the user. Then, take in n floats from the user and store them in a list. For instance, if the user enters 4, then the user will have to enter 4 numbers. Print the list and the mean.

n = int(input("Please enter a number: "))
floats = []
for x in range(n):
    floats.append(float(input(f"Please enter a number: ")))

mean = sum(floats) / n
print(f"The list of numbers are: {floats}")
print("The mean is: {mean}")


