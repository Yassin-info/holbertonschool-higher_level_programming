#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -3, -8]), -3)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([0, -5, 10, -3]), 10)

    def test_all_same(self):
        """Test with all elements the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)
        self.assertEqual(max_integer([5, 100, 50, 25]), 100)

    def test_with_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.1]), 3.9)
        self.assertEqual(max_integer([-1.5, -2.7, -0.5]), -0.5)

    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_zero_included(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-5, 0, -3]), 0)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)


if __name__ == '__main__':
    unittest.main()
