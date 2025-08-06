"""
-------------------------------------------------------
Exam: Simple Deques testing

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
from Deque_linked import Deque

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (8, 6, 7, 2, 7, 6, 8,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Deque values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Deque(values):
    """
    Testing helper method. Copies Python list values to a Deque.
    """
    source = Deque()
    for value in values:
        source.insert_front(value)
    return source


def test_reverse():
    """
    Tests the 'reverse' method.
    """
    print(SEP)
    print("Test 'reverse'")
    print()

    source = to_Deque(VALUES0)
    print(f"source: {to_python_list(source)}")
    source.reverse()
    print(f"source.reverse()")
    print(f"source: {to_python_list(source)}")
    print()


if __name__ == "__main__":
    """
    Remove Comment '#' from function calls to test
    """
    print("Deque_linked Testing")
    test_reverse()
