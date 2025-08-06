"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""
from functions import reroute

values_in = [1, 2, 3, 4]
opstring = "SSXXS"

values_out = reroute(opstring, values_in)

print("Values Out:", " ".join(map(str, values_out)))
