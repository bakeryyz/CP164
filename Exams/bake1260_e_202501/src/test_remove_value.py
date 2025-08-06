"""
-------------------------------------------------------
Exam: Simple Queues testing

See main code at bottom
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-04-15"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Queue_linked import Queue

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (3, 3, 7, 4, 4, 4, 5,)
VALUES2 = (3, 8, 6, 7, 6, 2, 4, 6,)
SEP = '-' * 60


def to_string(source):
    """
    Testing helper method. Copies List values to a string.
    """
    string = "_front > " + " > ".join(str(value) for value in source)

    if not string.endswith("> "):
        string += " > "
    string += "None"
    return string


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


def test_remove_value():
    """
    Tests the 'remove_value' method.
    """
    print(SEP)
    print("Test 'remove_value'")
    print()
    test_queues = (VALUES0, VALUES1, VALUES2,)

    for test_queue in test_queues:
        source = to_Queue(test_queue)
        print(f"source before: {to_string(source)}")
        print("source.remove_value(6)")
        source.remove_value(6)
        print(f"source after:  {to_string(source)}")
        print()


if __name__ == "__main__":
    print("Queue_linked Testing")
    test_remove_value()
