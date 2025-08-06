"""
-------------------------------------------------------
Exam: Simple List testing

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
from List_linked import List

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (4, 2, 7, 5, 0,)
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
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_List(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_common_node():
    """
    Tests the 'common_node' method.
    """
    print(SEP)
    print("Test 'common_node'")
    print()
    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    target = to_List(VALUES1)
    print(f"target: {to_python_list(target)}")
    node = source.common_node(target)
    print("node = source.common_node(target)")

    if node is None:
        print("node: None")
    else:
        print(f"node: {node._value}")
    print()
    # Connect target List to source List
    target._front._next._next = source._front._next._next
    print(f"source: {to_python_list(source)}")
    print(f"target: {to_python_list(target)}")
    node = source.common_node(target)
    print("node = source.common_node(target)")

    if node is None:
        print("node: None")
    else:
        print(f"node: {node._value}")


if __name__ == "__main__":
    print("List_linked Testing")
    test_common_node()
