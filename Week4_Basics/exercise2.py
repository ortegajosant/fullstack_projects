from sys import exit
# Exercise 2

ERROR_CODE = 1

# Request information from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
try:
    age = int(age)
except Exception as e:
    print('Age can only be an integer')
    exit(ERROR_CODE)

if age < 0:
    print('Age can only be a positive integer')
    exit(ERROR_CODE)

# Validate the age category
category = ''
if age < 2:
    category = "baby"
elif age < 12:
    category = "child"
elif age < 14:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 26:
    category = "young adult"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(f"{first_name} {last_name} is a {category}.")
