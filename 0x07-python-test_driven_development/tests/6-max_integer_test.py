"""
Unit tests for the max_integer function.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        result = max_integer([-1, -5, -3, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([1, -3, 5, -2, 4])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.0, 0.5, 3.0])
        self.assertEqual(result, 3.0)

    def test_strings(self):
        result = max_integer(["apple", "banana", "orange"])
        self.assertEqual(result, "orange")

    def test_mixed_types(self):
        result = max_integer([1, "apple", 3.5, "banana"])
        self.assertIsNone(result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_output(self, mock_stdout):
        max_integer([1, 2, 3, 4])
        self.assertEqual(mock_stdout.getvalue(), '4\n')

if __name__ == '__main__':
    unittest.main()
