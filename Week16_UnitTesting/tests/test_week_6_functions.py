import unittest
import sys

from io import StringIO
from week6.exercise3 import sum_list
from week6.exercise4 import reverse_string
from week6.exercise5 import count_case
from week6.exercise6 import sort_words_by_hyphen
from week6.exercise7 import is_prime, get_primes


class TestExercise3(unittest.TestCase):
    def test_sum_list_positive(self):
        # Preparation
        data = [1, 2, 3]
        expected = 6
        # Execution
        result = sum_list(data)
        # Assertion
        self.assertEqual(expected, result)

    def test_sum_list_negatives(self):
        # Preparation
        data = [-1, -2, -3]
        expected = -6
        # Execution
        result = sum_list(data)
        # Assertion
        self.assertEqual(expected, result)

    def test_sum_list_mixed(self):
        # Preparation
        data = [10, -5, 0, 5]
        expected = 10
        # Execution
        result = sum_list(data)
        # Assertion
        self.assertEqual(expected, result)


class TestExercise4(unittest.TestCase):
    def test_reverse_string_simple(self):
        # Preparation
        string = "hello"
        expected = "olleh"
        # Execution
        result = reverse_string(string)
        # Assertion
        self.assertEqual(expected, result)

    def test_reverse_string_with_spaces(self):
        # Preparation
        string = "hello world"
        expected = "dlrow olleh"
        # Execution
        result = reverse_string(string)
        # Assertion
        self.assertEqual(expected, result)

    def test_reverse_string_empty(self):
        # Preparation
        string = ""
        # Execution
        result = reverse_string(string)
        # Assertion
        self.assertEqual(string, result)


class TestExercise5(unittest.TestCase):
    def test_count_case_mixed(self):
        # Preparation
        captured = StringIO()
        string = "Hello World"
        # Execution
        sys.stdout = captured
        count_case(string)
        sys.stdout = sys.__stdout__
        # Assertion
        self.assertIn("There’s 2 upper cases and 8 lower cases", captured.getvalue())

    def test_count_case_all_upper(self):
        # Preparation
        captured = StringIO()
        string = "ABC"
        expected = "There’s 3 upper cases and 0 lower cases"
        # Execution
        sys.stdout = captured
        count_case(string)
        sys.stdout = sys.__stdout__
        # Assertion
        self.assertIn(expected, captured.getvalue())

    def test_count_case_all_lower(self):
        # Preparation
        captured = StringIO()
        string = "abc"
        expected_output = "There’s 0 upper cases and 3 lower cases"
        # Execution
        sys.stdout = captured
        count_case(string)
        sys.stdout = sys.__stdout__
        # Assertion
        self.assertIn(expected_output, captured.getvalue())


class TestExercise6(unittest.TestCase):
    def test_sort_words_by_hyphen_simple(self):
        # Preparation
        string = "banana-apple-cherry"
        expected = "apple-banana-cherry"
        # Execution
        result = sort_words_by_hyphen(string)
        # Assertion
        self.assertEqual(expected, result)

    def test_sort_words_by_hyphen_with_duplicates(self):
        # Preparation
        string = "dog-cat-dog-bird"
        expected = "bird-cat-dog-dog"
        # Execution
        result = sort_words_by_hyphen(string)
        # Assertion
        self.assertEqual(expected, result)

    def test_sort_words_by_hyphen_single_word(self):
        # Preparation
        string = "single"
        # Execution
        result = sort_words_by_hyphen(string)
        # Assertion
        self.assertEqual(string, result)

    def test_sort_words_by_hyphen_empty(self):
        # Preparation
        string = ""
        # Execution
        result = sort_words_by_hyphen(string)
        # Assertion
        self.assertEqual(string, result)

    def test_sort_words_by_hyphen_with_spaces(self):
        # Preparation
        string = "zebra- apple-pear"
        expected = " apple-pear-zebra"
        # Execution
        result = sort_words_by_hyphen(string)
        # Assertion
        self.assertEqual(expected, result)


class TestExercise7(unittest.TestCase):
    def test_is_prime_true(self):
        # Preparation
        n = 7
        # Execution
        result = is_prime(n)
        # Assertion
        self.assertTrue(result)

    def test_is_prime_false(self):
        # Preparation
        n = 9
        # Execution
        result = is_prime(n)
        # Assertion
        self.assertFalse(result)

    def test_is_prime_edge(self):
        # Preparation
        n = 1
        # Execution
        result = is_prime(n)
        # Assertion
        self.assertFalse(result)

    def test_get_primes_mixed(self):
        # Preparation
        nums = [2, 3, 4, 5, 6]
        expected_primes = [2, 3, 5]
        # Execution
        result = get_primes(nums)
        # Assertion
        self.assertEqual(expected_primes, result)

    def test_get_primes_none(self):
        # Preparation
        nums = [0, 1, 4, 6]
        expected_primes = []
        # Execution
        result = get_primes(nums)
        # Assertion
        self.assertEqual(expected_primes, result)

    def test_get_primes_all(self):
        # Preparation
        nums = [2, 3, 5, 7]
        # Execution
        result = get_primes(nums)
        # Assertion
        self.assertEqual(nums, result)


if __name__ == "__main__":
    unittest.main()
