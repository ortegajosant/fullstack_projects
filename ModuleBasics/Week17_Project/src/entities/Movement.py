EXPENSE_TYPE = "Expense"
INCOME_TYPE = "Income"


class Movement:
    def __init__(self, title: str, amount: float, category: str, type: str):
        self.category = category
        self.amount = amount
        self.title = title
        self.type = type

    def to_list(self):
        return [self.title, self.amount, self.category, self.type]

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
        }
