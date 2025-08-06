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
from functions import median_scores

# constants
with open("numbers.txt", "r") as fv:
    median = median_scores(fv)
    print(f"The median is: {median}")