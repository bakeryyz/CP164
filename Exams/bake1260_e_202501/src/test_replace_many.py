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


def test_replace_many():
    """
    Tests the 'replace_many' method.
    """
    print(SEP)
    print("Test 'replace_many'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.replace_many(9, -1)
    print(f"  After 'replace_many(9, -1)': {to_python_list(source)}")
    print()

    source = to_List([9] * 6)
    print(f"  List: {to_python_list(source)}")
    source.replace_many(9, 8)
    print(f"  After 'replace_many(9, 8)': {to_python_list(source)}")
    print()

    source = to_List(VALUES0)
    print(f"  List: {to_python_list(source)}")
    source.replace_many(6, 0)
    print(f"  After 'replace_many(6, 0)': {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    test_replace_many()
