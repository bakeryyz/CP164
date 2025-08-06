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

playlist = List()

playlist.prepend("GODS PLAN - DRAKE")

playlist.append("Imagine - John Lennon")

playlist.insert(1, "Not Like Us - Kendrick Lamar")

for each in playlist:
    print(each)