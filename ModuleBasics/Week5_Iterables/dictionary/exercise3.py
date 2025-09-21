employee = {
    "name": "Jose",
    "email": "jose@mail.com",
    "access_level": 5,
    "age": 28,
    "department": "IT",
    "position": "Software Engineer",
    "salary": 100,
    "hire_date": "2020-01-15",
    "manager": "Jose's Manager",
    "location": "CR",
}

print("Current dictionary:", employee)

list_of_keys = input("Enter the keys to delete, separated by commas: ").split(",")

for key in list_of_keys:
    key = key.strip()  # Remove any extra whitespace if present
    if key in employee:
        employee.pop(key)

print("Updated dictionary:", employee)
