try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    largest = number1

    if number2 > largest:
        largest = number2
    if number3 > largest:
        largest = number3

    print(f"The largest number is: {largest}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
