def is_prime(number):
    if number <= 1:
        return False

    # Following the method: Sieve of Eratosthenes
    number_sqrt = int(number**0.5)
    for i in range(2, number_sqrt + 1):
        if number % i == 0:
            return False
    return True


def get_primes(number_list):
    prime_list = []
    for number in number_list:
        if is_prime(number):
            prime_list.append(number)
    return prime_list


def request_numbers():
    user_input = input("Please enter a list of numbers separated by commas: ")
    number_list = [int(num.strip()) for num in user_input.split(",")]
    return number_list


def main():
    numbers = request_numbers()
    print(get_primes(numbers))  # Output: [7, 13, 67]


if __name__ == "__main__":
    main()
