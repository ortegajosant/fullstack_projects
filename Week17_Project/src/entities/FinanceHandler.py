from os import getcwd
from os.path import join
from src.logic.movements import validate_new_movement, save_movements, load_movements
from src.logic.categories import validate_category, save_categories, load_categories
from src.entities.Movement import EXPENSE_TYPE, INCOME_TYPE, Movement
from src.entities.Category import EXPENSE_TYPE, INCOME_TYPE, Category
from typing import List


class FinanceHandler:
    def __init__(self, data_directory=None):
        self._data_dir = self._set_data_directory(data_directory)
        self._movements = self._load_movements()
        self._categories = self._load_categories()

    @property
    def categories(self):
        return list({category.name for category in self._categories})

    @property
    def movements(self) -> List[Movement]:
        return [movement.to_list() for movement in self._movements]

    @movements.setter
    def movements(self, movements: List[Movement]):
        self._movements = movements

    @categories.setter
    def categories(self, categories: List[Category]):
        if not categories:
            raise ValueError("Categories cannot be empty.")
        self._categories = set(categories)

    def _set_data_directory(self, directory: str):
        if directory is not None:
            return directory
        current_dir = getcwd()
        data_dir = join(current_dir, "data")
        return data_dir

    def _add_movement(self, title: str, amount: float, category: str, type: str):
        movement = Movement(title, amount, category, type)
        self._movements.append(movement)
        save_movements(self._data_dir, self._movements)

    def _load_movements(self):
        movements = load_movements(self._data_dir)
        return [Movement(**m) for m in movements]

    def _load_categories(self):
        categories = load_categories(self._data_dir)
        return [Category(c) for c in categories]

    def add_category(self, name: str):
        validate_category(name, self.categories)
        self._categories.append(Category(name))
        save_categories(self._data_dir, self.categories)

    def add_expense(self, title: str, amount: str, category: str):
        validate_new_movement(title, amount, category)
        self._add_movement(
            amount=float(amount),
            category=category,
            title=title,
            type=EXPENSE_TYPE,
        )

    def add_income(self, title: str, amount: str, category: str):
        validate_new_movement(title, amount, category)
        self._add_movement(
            amount=float(amount),
            category=category,
            title=title,
            type=INCOME_TYPE,
        )
