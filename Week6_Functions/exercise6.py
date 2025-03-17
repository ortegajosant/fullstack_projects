def sort_words_by_hyphen(string):
    # Convert the string to a list of words
    words = string.split("-")
    # Sort the list alphabetically
    words.sort()
    # Convert the list back to a string with words separated by hyphens
    sorted_string = "-".join(words)
    return sorted_string


def main():
    string = "python-variable-funcion-computadora-monitor"
    result = sort_words_by_hyphen(string)
    print(result)


if __name__ == "__main__":
    main()
