"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-30"
-------------------------------------------------------
"""
from List_array import List

target = List()

target.append(10)
target.append(20)
target.append(30)

for i in target:
    print(i)

value_at_index_1 = target[1] 
print(f"Value at index 1: {value_at_index_1}")

target[1] = 25 
print("After setting index 1 to 25:")

for i in target:
    print(i)
