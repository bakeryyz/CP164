"""
-------------------------------------------------------
Exam: Simple BST testing

See main code at bottom
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-04-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
VALUES0 = (11, 7, 6, 9, 8, 15, 12, 18,)
VALUES1 = (2, 3, 1,)
VALUES2 = (11, 7, 13, 12, 18, 19,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies BST values to a Python list in levelorder
    """
    return source.levelorder()


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    bst = BST()

    for v in values:
        bst.insert(v)
    return bst


def test_shift_left():
    """
    Tests the '_shift_left' method.
    """
    print(SEP)
    print("Test '_shift_left'")
    print("(BST shown in level order)")
    print()
    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    source._root = source._shift_left(source._root)
    print("source._root = source._shift_left(source._root)")
    print(f"source: {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("BST_linked Testing")
    test_shift_left()
