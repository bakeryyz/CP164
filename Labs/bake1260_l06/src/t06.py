"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-02-12"
-------------------------------------------------------
"""
# Imports
from List_linked import List

my_list = List()
my_list.append("apple")
my_list.append("banana")

my_list.append("cherry")

item_at_index_1 = my_list[1]
print("Item at index 1:", item_at_index_1)

my_list[1] = "blueberry"
print("New item at index 1:", my_list[1])