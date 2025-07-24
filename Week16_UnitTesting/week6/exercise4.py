def reverse_string(string):
    reverse_chars = []
    for i in range(len(string) - 1, -1, -1):
        reverse_chars.append(string[i])
    # This can also be implemented by:
    # return s[::-1]
    # But it is more a "Pythonic" way of doing it
    return "".join(reverse_chars)


def main():
    input_string = "Hola mundo"
    reversed_string = reverse_string(input_string)
    print(reversed_string)  # Output: "odnum aloH"


if __name__ == "__main__":
    main()
