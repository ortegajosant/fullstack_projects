def print_params(function_name, *args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        print(f"Calling '{function_name}' without parameters")
    elif len(args) > 0:
        print(f"Calling '{function_name}' with={args}")
    if len(kwargs) > 0:
        print(f"Calling '{function_name}' with named parameters={kwargs}")


def print_params_and_return(func):
    def wrapper(*args, **kwargs):
        print_params(func.__name__, *args, **kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


@print_params_and_return
def sum(a, b):
    return a + b


@print_params_and_return
def greeting(name):
    return f"Hello, {name}!"


@print_params_and_return
def greet_user():
    return "Hello, User!"


def main():
    sum(10, 20)
    greeting(name="Ana")
    greet_user()


if __name__ == "__main__":
    main()
