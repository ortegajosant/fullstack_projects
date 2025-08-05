import unittest
from unittest.mock import patch, MagicMock
from src.entities.FinanceHandler import FinanceHandler
from src.entities.Category import Category
from src.entities.Movement import Movement, EXPENSE_TYPE, INCOME_TYPE


class TestFinanceHandler(unittest.TestCase):
    @patch("src.entities.FinanceHandler.getcwd", return_value="/tmp")
    @patch("src.entities.FinanceHandler.join", return_value="/tmp/data")
    @patch("src.entities.FinanceHandler.load_movements", return_value=[])
    @patch("src.entities.FinanceHandler.load_categories", return_value=[])
    def test_init_sets_data_dir_and_loads(
        self, mock_load_categories, mock_load_movements, mock_join, mock_getcwd
    ):
        handler = FinanceHandler()
        self.assertEqual(handler._data_dir, "/tmp/data")
        self.assertEqual(handler._movements, [])
        self.assertEqual(handler._categories, [])


    @patch("src.entities.FinanceHandler.load_movements")
    @patch("src.entities.FinanceHandler.load_categories")
    def test_set_data_directory_with_arg(self, *args):
        handler = FinanceHandler(data_directory="custom_dir")
        self.assertEqual(handler._data_dir, "custom_dir")

    @patch("src.entities.FinanceHandler.load_movements")
    @patch("src.entities.FinanceHandler.load_categories")
    @patch("src.entities.FinanceHandler.save_categories")
    @patch("src.entities.FinanceHandler.validate_category")
    def test_add_category(self, mock_validate_category, mock_save_categories, *args):
        handler = FinanceHandler(data_directory="dir")
        handler._categories = []
        handler.add_category("Food")
        mock_validate_category.assert_called_once()
        mock_save_categories.assert_called_once()

    @patch("src.entities.FinanceHandler.load_movements")
    @patch("src.entities.FinanceHandler.load_categories")
    @patch("src.entities.FinanceHandler.save_movements")
    @patch("src.entities.FinanceHandler.validate_new_movement")
    def test_add_expense(self, mock_validate_new_movement, mock_save_movements, *args):
        handler = FinanceHandler(data_directory="dir")
        handler._movements = []
        handler._add_movement = MagicMock()
        handler.add_expense("Lunch", "10", "Food")
        mock_validate_new_movement.assert_called_once_with("Lunch", "10", "Food")
        handler._add_movement.assert_called_once_with(
            amount=10.0, category="Food", title="Lunch", type=EXPENSE_TYPE
        )

    @patch("src.entities.FinanceHandler.load_movements")
    @patch("src.entities.FinanceHandler.load_categories")
    @patch("src.entities.FinanceHandler.save_movements")
    @patch("src.entities.FinanceHandler.validate_new_movement")
    def test_add_income(self, mock_validate_new_movement, mock_save_movements, *args):
        handler = FinanceHandler(data_directory="dir")
        handler._movements = []
        handler._add_movement = MagicMock()
        handler.add_income("Salary", "1000", "Work")
        mock_validate_new_movement.assert_called_once_with("Salary", "1000", "Work")
        handler._add_movement.assert_called_once_with(
            amount=1000.0, category="Work", title="Salary", type=INCOME_TYPE
        )


if __name__ == "__main__":
    unittest.main()
