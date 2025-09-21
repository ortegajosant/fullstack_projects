import unittest
import random

from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_small_list(self):
        # Preparation
        data = [5, 2, 9, 1, 5, 6]
        expected = sorted(data)

        # Execution
        bubble_sort(data)

        # Assertion
        self.assertEqual(expected, data)

    def test_large_list(self):
        # Preparation
        data = random.sample(range(1000), 200)
        expected = sorted(data)

        # Execution
        bubble_sort(data)

        # Assertion
        self.assertEqual(expected, data)

    def test_empty_list(self):
        # Preparation
        data = []
        expected = []

        # Execution
        bubble_sort(data)

        # Assertion
        self.assertEqual(expected, data)

    def test_non_list_parameter(self):
        # Preparation
        invalid_inputs = ["not a list", 123, None]

        # Execution & Assertion
        for invalid_input in invalid_inputs:
            with self.assertRaises(TypeError):
                bubble_sort(invalid_input)


if __name__ == "__main__":
    unittest.main()
