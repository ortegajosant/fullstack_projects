import unittest
from unittest.mock import patch, MagicMock
from src.logic.movements import (
    validate_new_movement,
    save_movements,
    load_movements,
    MOVEMENTS_FILE,
)


class TestMovements(unittest.TestCase):
    def test_validate_new_movement_valid(self):
        self.assertTrue(validate_new_movement("Salary", "1000", "Income"))

    def test_validate_new_movement_missing_fields(self):
        with self.assertRaises(ValueError):
            validate_new_movement("", "1000", "Income")
        with self.assertRaises(ValueError):
            validate_new_movement("Salary", "", "Income")
        with self.assertRaises(ValueError):
            validate_new_movement("Salary", "1000", "")

    def test_validate_new_movement_invalid_amount(self):
        with self.assertRaises(ValueError):
            validate_new_movement("Salary", "abc", "Income")
        with self.assertRaises(ValueError):
            validate_new_movement("Salary", "10.0.0", "Income")

    @patch("src.logic.movements.save_file")
    @patch("src.logic.movements.join", return_value="test_path/movements.json")
    def test_save_movements(self, _, mock_save_file):
        mock_movement = MagicMock()
        mock_movement.to_dict.return_value = {
            "title": "Salary",
            "amount": 1000,
            "category": "Income",
            "type": "INCOME",
        }
        save_movements("test_path", [mock_movement])
        mock_save_file.assert_called_once_with(
            "test_path/movements.json", [mock_movement.to_dict()]
        )

    @patch("src.logic.movements.load_file")
    @patch("src.logic.movements.join", return_value="test_path/movements.json")
    def test_load_movements_success(self, _, mock_load_file):
        mock_load_file.return_value = [
            {"title": "Salary", "amount": 1000, "category": "Income", "type": "INCOME"}
        ]
        result = load_movements("test_path")
        self.assertEqual(
            result,
            [
                {
                    "title": "Salary",
                    "amount": 1000,
                    "category": "Income",
                    "type": "INCOME",
                }
            ],
        )

    @patch("src.logic.movements.load_file", side_effect=FileNotFoundError)
    @patch("src.logic.movements.save_file")
    @patch("src.logic.movements.join", return_value="test_path/movements.json")
    def test_load_movements_file_not_found(
        self, mock_join, mock_save_file, mock_load_file
    ):
        result = load_movements("test_path")
        self.assertEqual(result, [])
        mock_save_file.assert_called_once_with("test_path/movements.json", [])

    @patch("src.logic.movements.load_file", side_effect=Exception("Some error"))
    @patch("src.logic.movements.join", return_value="test_path/movements.json")
    def test_load_movements_other_exception(self, mock_join, mock_load_file):
        with self.assertRaises(Exception) as context:
            load_movements("test_path")
        self.assertIn("Error loading movements", str(context.exception))


if __name__ == "__main__":
    unittest.main()
