"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

test_strings = [
    "racecar",
    "Otto"
]


# testing the function on each test string
for string in test_strings:
    result = is_palindrome_stack(string)
    print(f"{string}: {result}")
