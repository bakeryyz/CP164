"""
-------------------------------------------------------
Exam: Simple Queues testing

See main code at bottom
Remove '#' from lines to test
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2024-11-26"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Queue_linked import Queue

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (3, 3, 7, 4, 4, 4, 5,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Queue values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Queue(values):
    """
    Testing helper method. Copies Python list values to a Queue.
    """
    source = Queue()
    for value in values:
        source.insert(value)
    return source


def test_append_queue():
    """
    Tests the '_append_queue ' method.
    """
    print(SEP)
    print("Test '_append_queue '")
    print()

    source = to_Queue(VALUES0)
    print(f"source: {to_python_list(source)}")
    target = to_Queue(VALUES1)
    print(f"target: {to_python_list(target)}")
    target._append_queue(source)
    print("target._append_queue(source)")
    print(f"target: {to_python_list(target)}")
    print()


if __name__ == "__main__":
    """
    Remove Comment '#' from function calls to test
    """
    print("Queue_linked Testing")
    test_append_queue()
