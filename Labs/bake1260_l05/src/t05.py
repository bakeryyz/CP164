"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-02-05"
-------------------------------------------------------
"""
# Imports
import unittest
from functions import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()