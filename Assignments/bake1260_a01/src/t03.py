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
from functions import file_analyze

# constants
with open("baseball.txt", "r") as fv:
    upp, low, dig, whi, rem = file_analyze(fv)
    print(f"Upper Cases: {upp}")
    print(f"Lower Cases: {low}")
    print(f"Digits: {dig}")
    print(f"White Spaces: {whi}")
    print(f"Everything Else: {rem}")
