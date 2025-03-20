try:
    my_list = [int(x) for x in input("Enter the list elements separated by space: ").split()]
except ValueError:
    print("Please enter valid integers.")
    my_list = [7, 3, 6, 1, 4]
    print("Using a default list.", my_list)

# Using while loop instead of for loop to iterate over the list and use pop() to remove even numbers
# from the list. The for loop is not used because the length of the list changes as elements are removed.
i = 0
while i < len(my_list):
    if my_list[i] % 2 != 0:
        my_list.pop(i)
    else:
        i += 1

print(my_list)
