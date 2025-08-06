"""
-------------------------------------------------------
Exam: Simple List testing

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
from List_linked import List


# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (4, 2, 7, 5, 0,)
SEP = '-' * 60


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


def get_nodes(source):
    """
    Creates a list of nodes of a List
    """
    nodes = []
    curr = source._front

    while curr is not None:
        nodes.append(curr)
        curr = curr._next
    return nodes


def test_split_alt():
    """
    Tests the 'split_alt' method.
    """
    print(SEP)
    print("Test 'split_alt'")
    print()

    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_alt()
    print("target1, target2 = source.split_alt()")
    print(f"source: {to_python_list(source)}")
    print(f"target1: {to_python_list(target1)}")
    print(f"target2: {to_python_list(target2)}")
    print()


def test_swap():
    """
    Tests the '_swap' method.
    """
    print(SEP)
    print("Test '_swap'")
    print()
    source = to_List(VALUES0)
    # Create a list of nodes for testing
    print(f"source: {to_python_list(source)}")
    print("swap front and 2nd node")
    nodes = get_nodes(source)
    pln = None
    prn = nodes[0]
    source._swap(pln, prn)
    print(f"source: {to_python_list(source)}")
    print("swap front and rear")
    nodes = get_nodes(source)
    pln = None
    prn = nodes[-2]
    source._swap(pln, prn)
    print(f"source: {to_python_list(source)}")
    print("swap front._next and previous to rear")
    nodes = get_nodes(source)
    pln = nodes[0]
    prn = nodes[-3]
    source._swap(pln, prn)
    print(f"source: {to_python_list(source)}")


if __name__ == "__main__":
    """
    Remove Comment '#' from function calls to test
    """
    print("List_linked Testing")
    test_split_alt()
    test_swap()

