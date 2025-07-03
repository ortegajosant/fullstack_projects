def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def main():
    numbers_list = [4, 6, 2, 29]
    result = sum_list(numbers_list)
    print(result)


if __name__ == "__main__":
    main()
