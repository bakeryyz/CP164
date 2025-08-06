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
from functions import vowel_count

class TestVowelCount(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(vowel_count("hello"), 2)
        self.assertEqual(vowel_count("AEIOU"), 5)
        self.assertEqual(vowel_count("xyz"), 0)
        self.assertEqual(vowel_count(""), 0)
        self.assertEqual(vowel_count("beautiful"), 5)

if __name__ == "__main__":
    unittest.main()