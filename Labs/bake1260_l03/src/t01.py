"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-23"
-------------------------------------------------------
"""
from Queue_array import Queue

def test_queue():
    q = Queue()

    print("Queue is empty:", q.is_empty())

    for value in [10, 20, 30, 40, 50]:
        q.insert(value)

    print("Length of the queue:", len(q))
    print("Peeking at the front of the queue:", q.peek())

    while not q.is_empty():
        print("Removed:", q.remove())

    print("Queue is empty after all removals:", q.is_empty())

    try:
        q.remove()
    except AssertionError as e:
        print("Caught an error:", e)

    try:
        q.peek()
    except AssertionError as e:
        print("Caught an error:", e)

if __name__ == "__main__":
    test_queue()
