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

target.append(10)
target.append(20)
target.append(30)

target.insert(1, 15)  

for i in target:
    print(i)

removed_value = target.remove(20)  
print(f"Removed value: {removed_value}")

for i in target:
    print(i)