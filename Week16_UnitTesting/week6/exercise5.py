def count_case(s):
    upper_count = 0
    lower_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")


def get_text():
    text = input("Please enter the text: ")
    if not text:
        text = "I love Nación Sushi"
    return text


def main():
    text = get_text()
    count_case(text)


if __name__ == "__main__":
    main()
