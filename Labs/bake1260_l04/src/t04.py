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

target = List()

target.append(10)
target.append(20)
target.append(30)
target.append(20)

for i in target:
    print(i)

index_value = target.index(20)  
print(f"Index of 20: {index_value}")

found_value = target.find(30) 
print(f"Found value: {found_value}")

print(f"Contains 10: {10 in target}")
print(f"Contains 40: {40 in target}")

count_20 = target.count(20) 
print(f"Count of 20: {count_20}")

max_value = target.max()  
print(f"Max value: {max_value}")

min_value = target.min()  
print(f"Min value: {min_value}")
