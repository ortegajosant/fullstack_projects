global_variable = "I am a global variable"


def inner_function():
    inner_variable = "I am an inner variable"
    print(inner_variable)


def try_to_change_global_variable():
    global_variable = "I am trying to change the global variable"
    print(global_variable)


def change_global_variable():
    global global_variable
    global_variable = "I have changed the value of the global variable"
    print(global_variable)


def main():
    # 1. Example about variable scope in Python with local variable
    # Attempt to access a variable defined inside a function from outside
    inner_function()
    try:
        print(inner_variable)
    except NameError as e:
        print(f"Error: {e}")
    print("\n" + "-" * 50 + "\n")

    # 2. Example about variable scope in Python with global variable
    # Attempt to access a global variable from a function and change its value
    print(global_variable)
    try_to_change_global_variable()
    print(f"\nNo change in the global variable: {global_variable}\n")

    change_global_variable()
    print(f"\nGlobal variable has been changed: {global_variable}")


if __name__ == "__main__":
    main()
