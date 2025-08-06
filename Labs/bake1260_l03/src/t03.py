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
from Priority_Queue_array import Priority_Queue
from utilities import queue_test, array_to_pq, pq_to_array, priority_queue_test

def test_queue():
    q = Queue()
    data = [10, 20, 30, 40, 50]

    print(q.is_empty())
    for value in data:
        q.insert(value)
    print(q.is_empty())
    print(q.peek())
    while not q.is_empty():
        print(q.remove())
    print(q.is_empty())

def test_priority_queue():
    pq = Priority_Queue()
    data = [50, 40, 30, 20, 10]

    print(pq.is_empty())
    for value in data:
        pq.insert(value)
    print(pq.is_empty())
    print(pq.peek())
    while not pq.is_empty():
        print(pq.remove())
    print(pq.is_empty())

def test_array_to_pq_and_pq_to_array():
    pq = Priority_Queue()
    source = [100, 90, 80, 70, 60]
    target = []

    array_to_pq(pq, source)
    print("Source after array_to_pq:", source)
    pq_to_array(pq, target)
    print("Target after pq_to_array:", target)

if __name__ == "__main__":
    print("Testing Queue:")
    test_queue()
    print("\nTesting Priority Queue:")
    test_priority_queue()
    print("\nTesting array_to_pq and pq_to_array:")
    test_array_to_pq_and_pq_to_array()
