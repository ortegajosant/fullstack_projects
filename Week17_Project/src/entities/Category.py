EXPENSE_TYPE = "Expense"
INCOME_TYPE = "Income"


class Category:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not new_name:
            raise ValueError("Category name cannot be empty.")
        self._name = new_name
