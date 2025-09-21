list_a = input("Enter the first list of keys, separated by commas: ").split(",")
list_b = input("Enter the second list of values, separated by commas: ").split(",")

if len(list_a) != len(list_b):
    print("Both lists must have the same length")
    list_a = ["first_name", "last_name", "role"]
    list_b = ["Alek", "Castillo", "Software Engineer"]

result = {}
for i in range(len(list_a)):
    result[list_a[i]] = list_b[i]

print(result)
