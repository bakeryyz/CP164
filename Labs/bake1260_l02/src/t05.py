"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-17"
-------------------------------------------------------
"""

from utilities import array_to_stack
from Stack_array import Stack

def test_array_to_stack():
    stack = Stack()
    source = [1, 2, 3]
    array_to_stack(stack, source)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    test_array_to_stack()
