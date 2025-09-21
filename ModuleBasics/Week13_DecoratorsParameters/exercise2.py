def validate_params(*args):
    for arg in args:
        if isinstance(arg, (int, float)):
            continue
        raise TypeError(
            f"All positional parameters must be numbers: Value {arg} of type {type(arg)}"
        )


def validate_named_params(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            continue
        raise TypeError(
            f"All named parameters must be numbers: Parameter {key}: {value} of type {type(value)}"
        )


def check_numeric_params(func):
    def wrapper(*args, **kwargs):
        validate_params(*args)
        validate_named_params(**kwargs)
        return func(*args, **kwargs)

    return wrapper


@check_numeric_params
def add(a, b):
    return a + b


@check_numeric_params
def multiply(a, b, c=1):
    return a * b * c


def main():
    try:
        print("add(2, '3'):", add(2, "3"))
    except TypeError as e:
        print("Error:", e)
    print("add(2, 3):", add(2, 3))
    print("multiply(2, 3):", multiply(2, 3))
    try:
        print("multiply(2, 2, '3'):", multiply(2, 2, c="3"))
    except TypeError as e:
        print("Error:", e)
    print("multiply(2, 3, c=4):", multiply(2, 3, c=4))


if __name__ == "__main__":
    main()
