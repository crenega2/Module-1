#Take in a row number from 1 to 5 inclusive and a column number from 1 to 5. Print out a grid of 0s, but in the row and column entered by the user, print a 1.

row = int(input("Please enter the row number 1-5: "))
column = int(input("Please enter the column number 1-5: "))

for i in range(1,6):
    for x in range(1,6):
        # Puts a 1 where the user chose the row and column 
        if i == row and x == column:
            print("1", end = ' ')
        else:
            print("o", end = ' ')
    # Ends the for loop iteration and makes a new line        
    print()