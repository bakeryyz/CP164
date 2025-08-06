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
from Stack_array import Stack
from functions import stack_split_alt

source = Stack()
source.push(8)
source.push(14)
source.push(12)
source.push(9)
source.push(8)
source.push(7)
source.push(5)
target1, target2 = stack_split_alt(source)
print(target1._values)
print(target2._values)
