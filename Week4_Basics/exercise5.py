import sys

try:
    n = int(input("Enter the number of student grades: "))
    if n <= 0:
        print("The number of grades must be greater than zero.")
        sys.exit()

    passed = 0
    failed = 0
    total_sum = 0
    passed_sum = 0
    failed_sum = 0

    for i in range(n):
        grade = float(input(f"Enter grade {i + 1}: "))
        total_sum += grade

        if grade > 70:
            passed += 1
            passed_sum += grade
        else:
            failed += 1
            failed_sum += grade

    total_average = total_sum / n
    passed_average = passed_sum / passed if passed > 0 else 0
    failed_average = failed_sum / failed if failed > 0 else 0

    print(f"Number of passed grades: {passed}")
    print(f"Number of failed grades: {failed}")
    print(f"Average of all grades: {total_average}")
    print(f"Average of passed grades: {passed_average}")
    print(f"Average of failed grades: {failed_average}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
