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

def array_to_list(llist, source):
    while len(source) > 0:
        llist.append(source.pop(0))
    return None

def list_to_array(llist, target):
    while len(llist) > 0:
        target.append(llist.pop(0))
    return None

target = List()
source = [1, 2, 3, 4, 5]
print("Initial source list:", source)

array_to_list(target, source)

print("\nAfter array_to_list:")
print("List:", [i for i in target])
print("Source (should be empty):", source)

llist = List()
target = [10, 20, 30]
print("\nInitial target list:", target)

list_to_array(llist, target)

print("\nAfter list_to_array:")
print("List (should be empty):", [i for i in llist])
print("Target (should contain 10, 20, 30):", target)
