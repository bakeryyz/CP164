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
from functions import queue_combine

# Constants

q1 = Queue(3)
q2 = Queue(4)

q1.insert(1)
q1.insert(2)
q1.insert(3)

q2.insert(4)
q2.insert(5)
q2.insert(6)
q2.insert(7)

print("Before combine:")
print("Queue 1:", end=" ")
for i in range(q1._count):
    print(q1._values[(q1._front + i) % q1._max_size], end=" ")
print("\nQueue 2:", end=" ")
for i in range(q2._count):
    print(q2._values[(q2._front + i) % q2._max_size], end=" ")
print("\n")

target = queue_combine(q1, q2)

print("After combine:")
print("Target:", end=" ")
for i in range(target._count):
    print(target._values[(target._front + i) % target._max_size], end=" ")
print("\n")
