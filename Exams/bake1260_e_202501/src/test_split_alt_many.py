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


def test_split_alt_many():
    """
    Tests the 'split_alt_many' method.
    """
    print(SEP)
    print("Test 'split_alt_many'")
    print()

    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    targets = source.split_alt_many(1)
    print("targets = source.split_alt_many(1)")

    for i in range(len(targets)):
        print(f"  targets[{i}]: {to_python_list(targets[i])}")
    print()
    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    targets = source.split_alt_many(3)
    print("targets = source.split_alt_many(1)")

    for i in range(len(targets)):
        print(f"  targets[{i}]: {to_python_list(targets[i])}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    test_split_alt_many()
