# write a script that takes in a grade from 0-100 inclusive (include both 0 and 100 in the range). Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.

number = int(input("Please enter your grade: "))
print(number)

if number >= 90:
    print("You got an A!")
elif number >= 80 and number <= 89:
    print("You got a B")
elif number >= 70 and number <= 79:
    print("You got a C")
elif number >= 60 and number <= 69:
    print("You got a D")
else:
    print("You got a F")
