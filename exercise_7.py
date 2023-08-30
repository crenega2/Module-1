#Take in integers until the user types "QUIT" and store the numbers in a list. Assume any input other than "QUIT" is a valid integer. Create another list of just the even numbers and print both lists.

#I am not sure why this sin't working. I checked with bing AI and it isn't sure either. I put it in coding rooms, and it runs correctly. It won't leave the while loop in VS code
numbers = None
list = []
while(numbers != "quit"): 
    numbers = (input("Please enter a number or type 'QUIT' to quit: "))
    if numbers != "quit":
        list.append(int(numbers))

list2 = []
for x in range(len(list)):
    if list[x] % 2: 
        print(x)
    else:
        list2.append(list[x])
print(list)
print(list2)
