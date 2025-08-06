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
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

# Test Deque + Values! :)
check = Deque()
values = [1, 9, 8, 3, 5, 7, 4, 10]

for i in values:
    check.insert_rear(i)

Sorts.gnome_sort(check)

print("Sorted array: ")
for i in check:
    print(i)