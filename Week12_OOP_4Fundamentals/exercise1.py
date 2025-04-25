class BankAccount:
    INSUFFICIENT_FUNDS_MSG = "Insufficient funds."
    WITHDRAWAL_AMOUNT_MSG = "Withdrawal amount must be positive."

    def __init__(self, balance=0):
        self.balance = balance

    def __validate_balance(self, new_balance, actual_balance, msg):
        if new_balance > actual_balance:
            raise ValueError(msg)
        return True

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def is_amount_positive(self, amount):
        return amount > 0

    def withdraw(self, amount):
        if amount > 0:
            self.__validate_balance(amount, self.balance, self.INSUFFICIENT_FUNDS_MSG)
            self.balance -= amount
            return amount
        raise ValueError(self.WITHDRAWAL_AMOUNT_MSG)


class SavingsAccount(BankAccount):
    MIN_FOUNDS_MSG = "Insufficient funds. Minimum balance required."

    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.is_amount_positive(amount):
            new_balance = self.balance - amount
            self.__validate_balance(self.min_balance, new_balance, self.MIN_FOUNDS_MSG)
            self.__validate_balance(new_balance)
            self.balance = new_balance
            return amount
        raise ValueError(self.WITHDRAWAL_AMOUNT_MSG)


def main():
    # Test BankAccount
    print("Testing BankAccount:")
    account = BankAccount(100)
    print(f"Initial balance: {account.balance}")
    account.deposit(50)
    print(f"Balance after deposit of 50: {account.balance}")
    try:
        account.withdraw(30)
        print(f"Balance after withdrawal of 30: {account.balance}")
    except ValueError as e:
        print(e)
    try:
        account.withdraw(150)
    except ValueError as e:
        print(f"Error: {e}")

    # Test SavingsAccount
    print("\nTesting SavingsAccount:")
    savings = SavingsAccount(200, min_balance=50)
    print(f"Initial balance: {savings.balance}, Minimum balance: {savings.min_balance}")
    savings.deposit(100)
    print(f"Balance after deposit of 100: {savings.balance}")
    try:
        savings.withdraw(200)
        print(f"Balance after withdrawal of 200: {savings.balance}")
    except ValueError as e:
        print(f"Error: {e}")

    print(f"Try to withdraw: 300")
    try:
        savings.withdraw(300)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
