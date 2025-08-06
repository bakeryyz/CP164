"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-08"
-------------------------------------------------------
"""
# Imports
from functions import find_subs

# constants
string = input("String: ")
substring = input("Substring: ")
indices = find_subs(string, substring)
print(f"Locations: {str(indices)}")