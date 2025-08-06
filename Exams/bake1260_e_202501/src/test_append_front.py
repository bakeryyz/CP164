"""
-------------------------------------------------------
Exam: Simple Deques testing

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
from Deque_linked import Deque

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (3, 8, 9, 7, 9, 8, 3,)
VALUES2 = (3, 5, 5, 5, 8, 6, 9, 6,)
SEP = '-' * 60


def to_string(source):
    """
    Testing helper method. Copies List values to a string.
    """
    string = "_front > " + " <> ".join(str(value) for value in source)
    string += " < _rear"
    return string


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


def test_append_front():
    """
    Tests the 'append_front' method.
    """
    print(SEP)
    print("Test 'append_front'")
    print()
    test_deques = (VALUES0, VALUES1, VALUES2,)

    for test_deque in test_deques:
        source = to_Deque(test_deque)
        print(f"Deque: {to_python_list(source)}")
        source.append_front()
        print(f"After 'append_front': {to_python_list(source)}")
        print()


if __name__ == "__main__":
    print("Deque_linked Testing")
    test_append_front()
