import unittest
from unittest.mock import patch
from src.logic.categories import (
    validate_category,
    save_categories,
    load_categories,
    CATEGORIES_FILE,
    CATEGORIES_KEY,
)


class TestCategories(unittest.TestCase):
    def test_validate_category_valid(self):
        self.assertTrue(validate_category("Food", ["Work", "Transport"]))

    def test_validate_category_empty(self):
        with self.assertRaises(ValueError):
            validate_category("", ["Work", "Transport"])

    def test_validate_category_duplicate(self):
        with self.assertRaises(ValueError):
            validate_category("Food", ["Food", "Transport"])

    @patch("src.logic.categories.save_file")
    @patch("src.logic.categories.join", return_value="test_path/categories.json")
    def test_save_categories(self, mock_join, mock_save_file):
        categories = ["Food", "Transport"]
        save_categories("test_path", categories)
        mock_save_file.assert_called_once_with(
            "test_path/categories.json", {CATEGORIES_KEY: categories}
        )

    @patch(
        "src.logic.categories.load_file",
        return_value={CATEGORIES_KEY: ["Food", "Transport"]},
    )
    @patch("src.logic.categories.join", return_value="test_path/categories.json")
    def test_load_categories_success(self, mock_join, mock_load_file):
        result = load_categories("test_path")
        self.assertEqual(result, ["Food", "Transport"])

    @patch("src.logic.categories.load_file", side_effect=FileNotFoundError)
    @patch("src.logic.categories.save_categories")
    @patch("src.logic.categories.join", return_value="test_path/categories.json")
    def test_load_categories_file_not_found(
        self, mock_join, mock_save_categories, mock_load_file
    ):
        result = load_categories("test_path")
        self.assertEqual(result, [])
        mock_save_categories.assert_called_once_with("test_path", [])

    @patch("src.logic.categories.load_file", side_effect=Exception("Some error"))
    @patch("src.logic.categories.join", return_value="test_path/categories.json")
    def test_load_categories_other_exception(self, mock_join, mock_load_file):
        with self.assertRaises(Exception) as context:
            load_categories("test_path")
        self.assertIn("Error loading categories", str(context.exception))

    @patch("src.logic.categories.load_file", return_value={"wrong_key": ["Food"]})
    @patch("src.logic.categories.join", return_value="test_path/categories.json")
    def test_load_categories_invalid_format(self, mock_join, mock_load_file):
        with self.assertRaises(ValueError):
            load_categories("test_path")


if __name__ == "__main__":
    unittest.main()
