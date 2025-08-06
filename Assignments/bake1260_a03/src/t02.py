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
from functions import split_alt

source_stack = Stack()
for i in range(1, 13):
    source_stack.push(i)

target1, target2 = split_alt(source_stack)

print("Target 1:", " ".join(map(str, target1._values)))
print("Target 2:", " ".join(map(str, target2._values)))

