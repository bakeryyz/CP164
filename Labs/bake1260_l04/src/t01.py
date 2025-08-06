"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-28"
-------------------------------------------------------
"""
from List_array import List

target = List()

target.append(1)
target.append(1)
target.append(1)

for i in target:
    print(i)

test = target._is_valid_index(-3)
print(test)
print(target._values[-3])
