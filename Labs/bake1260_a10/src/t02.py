"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts

# Test List + Values!
check = List()
values = [1, 9, 8, 3, 5, 7, 4, 10]

for i in values:
    check.append(i)

Sorts.radix_sort(check)
print("Sorted array: ")
for i in check:
    print(i)
