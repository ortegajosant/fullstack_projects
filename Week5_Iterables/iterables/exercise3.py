# Example of swapping the first and last elements of a list
try:
    my_list = [int(x) for x in input("Enter the list elements separated by space: ").split()]
except ValueError:
    print("Please enter valid integers.")
    my_list = [7, 3, 6, 1, 4]
    print("Using a default list.", my_list)

# Swap the first and last elements of the list
if len(my_list) > 1:
    last_index = len(my_list) - 1
    first_index = 0
    first_element = my_list[first_index]
    last_element = my_list[last_index]
    my_list[first_index] = last_element
    my_list[last_index] = first_element

print(my_list)  # [7, 3, 6, 1, 4]
