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
from Queue_circular import Queue

# Constants

queue1 = Queue()
queue2 = Queue()

queue1.insert(1)
queue1.insert(2)
queue1.insert(3)

queue2.insert(1)
queue2.insert(2)
queue2.insert(3)

print(queue1 == queue2)

# Test Queues with different number of elements
queue1.insert(4)

print(queue1 != queue2)

# Test Queues with different values
queue2.insert(5)

print(queue1 != queue2)
