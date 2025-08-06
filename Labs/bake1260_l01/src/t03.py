"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
Section: CP164 C
__updated__ = "2025-01-06"
-------------------------------------------------------
"""
# Imports
from Movie import Movie


m1 = Movie('T1', 2000, 'D1', 5, [3, 4, 5, 8])
string = m1.genres_menu()
print(string)
