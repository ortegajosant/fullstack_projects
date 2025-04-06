class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return amount
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount > 0:
            new_balance = self.balance - amount
            if new_balance >= self.min_balance:
                self.balance = new_balance
                return amount
            else:
                raise ValueError("Withdrawal would put balance below minimum balance.")
        else:
            raise ValueError("Withdrawal amount must be positive.")


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
