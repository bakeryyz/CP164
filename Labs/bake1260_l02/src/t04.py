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
from Stack_array import Stack

def test_peek():
    stack = Stack()
    stack.push(10)
    print(stack.peek())

if __name__ == "__main__":
    test_peek()
