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
from functions import postfix

test_postfix = [
    "4 5 + 12 * 2 3 * -",
    "12 5 -",
    "2 3 4 * + 5 *",
    "1 2 + 3 4 - *",
    "5 1 2 + 4 * + 3 -"
]

# testing the function on each postfix expression
for postfix_expression in test_postfix:
    result = postfix(postfix_expression)
    print(f"{postfix_expression}: {result}")
