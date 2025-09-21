numbers = []

# Ask the user for 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Find the highest number
highest_number = numbers[0]
for num in numbers[1:]:
    if num > highest_number:
        highest_number = num

# Display the numbers entered and the highest number
print("Numbers entered:", numbers)
print("The highest number is:", highest_number)
