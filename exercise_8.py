#Take in 10 integers from user. Create a new list with only elements which appear once. Print both lists.

list = []
for x in range(10):
    numbers = int(input(f"Please enter number {x+1}: "))
    list.append(numbers)

list2 = []
for x in list:
    if list.count(x) == 1:
        list2.append(x)
print(f"The original list: {list}")
print(f"The new list: {list2}")

