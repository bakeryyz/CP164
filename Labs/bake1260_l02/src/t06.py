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
from utilities import stack_to_array
from Stack_array import Stack

def test_stack_to_array():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    target = []
    stack_to_array(stack, target)
    print(target)

if __name__ == "__main__":
    test_stack_to_array()
