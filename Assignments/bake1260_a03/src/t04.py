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
from Stack_array import Stack
from functions import reverse

source_stack = Stack()
for i in range(1, 6):
    source_stack.push(i)

reverse(source_stack)

print("Reversed Stack:", " ".join(map(str, source_stack._values)))
