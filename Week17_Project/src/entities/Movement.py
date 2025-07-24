EXPENSE_TYPE = "Expense"
INCOME_TYPE = "Income"


class Movement:
    def __init__(self, title: str, amount: float, category: str, type: str):
        self.category = category
        self.amount = amount
        self.title = title
        self.type = type

    def get_movement_info(self):
        return [self.title, self.amount, self.category, self.type]
