ERROR_MSG_INVALID_OPTION = "Opción inválida. Por favor, ingrese un número del 1 al 6."
ERROR_MSG_INVALID_NUMBER = "Número inválido. Por favor, ingrese un número válido."
ERROR_MSG_ZERO_DIVISION = "División por cero."


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError(ERROR_MSG_ZERO_DIVISION)
    return first_number / second_number


def display_menu():
    print("\nSeleccione una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Salir")


def get_option():
    try:
        return int(input("Opción: "))
    except ValueError:
        print(ERROR_MSG_INVALID_OPTION)
        return None


def get_number():
    try:
        return float(input("Ingrese el nuevo número: "))
    except ValueError:
        print(ERROR_MSG_INVALID_NUMBER)
        return None


def process_option(option, first_number=0):
    if option == 5:
        print("Borrando resultado actual.")
        return 0
    result = 0
    try:
        second_number = get_number()
        if second_number is None:
            raise ValueError("El número ingresado no es válido.")
        if option == 1:
            result = add(first_number, second_number)
        elif option == 2:
            result = subtract(first_number, second_number)
        elif option == 3:
            result = multiply(first_number, second_number)
        elif option == 4:
            result = divide(first_number, second_number)
    except Exception as e:
        print(f"Error al procesar la opción {option}: {e}")
    return result


def main():
    current_result = 0
    while True:
        display_menu()

        option = get_option()
        if option is None:
            continue

        if option == 6:
            print("Saliendo de la calculadora.")
            break

        if option not in [1, 2, 3, 4, 5]:
            print(ERROR_MSG_INVALID_OPTION)
            continue

        current_result = process_option(option, current_result)
        print(f"Resultado actual: {current_result}")


if __name__ == "__main__":
    main()
