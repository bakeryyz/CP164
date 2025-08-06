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
from functions import recurse

class TestRecurse(unittest.TestCase):
    def test_recurse(self):
        self.assertEqual(recurse(0, 0), 0)
        self.assertEqual(recurse(1, 0), 1)
        self.assertEqual(recurse(0, 1), -1)
        self.assertEqual(recurse(2, 1), 1)
        self.assertEqual(recurse(-1, 2), -3)

if __name__ == "__main__":
    unittest.main()