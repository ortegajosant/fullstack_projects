from .movements import validate_new_movement, save_movements
from .categories import validate_categories, save_categories
from entities.Movement import EXPENSE_TYPE, INCOME_TYPE, Movement
from typing import List


class FinanceHandler:
    def __init__(self):
        self.movements: List[Movement] = None
        self.categories: set = None

    @property
    def categories(self) -> List[str]:
        return list(self.categories)

    @property
    def movements(self) -> List[Movement]:
        return [movement.get_movement_info() for movement in self.movements]

    def _add_movement(self, title: str, amount: float, category: str, type: str):
        movement = Movement(title, amount, category, type)
        self.movements.append(movement)

    def load_movements(self, movements: List[List]):
        self.movements = [Movement(*m) for m in movements]
        self.categories = {m.category for m in self.movements}

    def load_categories(self, categories: List[str]):
        self.categories = set(categories)

    def add_category(self, category: str):
        self.categories.add(category)

    def add_expense(self, title: str, amount: str, category: str):
        validate_new_movement(title, amount, category)
        self.add_movement(
            amount=float(amount),
            category=category,
            title=title,
            type=EXPENSE_TYPE,
        )

    def add_income(self, title: str, amount: str, category: str):
        validate_new_movement(title, amount, category)
        self.add_movement(
            amount=float(amount),
            category=category,
            title=title,
            type=INCOME_TYPE,
        )
