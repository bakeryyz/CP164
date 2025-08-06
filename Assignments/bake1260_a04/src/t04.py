"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-28"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

# Constants

# Test with empty source queues
source1 = Queue()
source2 = Queue()
target = Queue()
target.combine(source1, source2)
print(target.is_empty() == True)

# Test with non-empty source queues
source1 = Queue()
source2 = Queue()
target = Queue()
source1.insert(1)
source1.insert(3)
source2.insert(2)
source2.insert(4)
target.combine(source1, source2)
result = [target.remove() for i in range(target._count)]
print(result == [1, 2, 3, 4])
