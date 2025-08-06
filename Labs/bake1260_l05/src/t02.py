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
from functions import gcd

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(27, 9), 9)
        self.assertEqual(gcd(17, 17), 17)

if __name__ == "__main__":
    unittest.main()
