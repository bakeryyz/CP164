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


def test_heavy_right():
    """
    Tests the 'heavy_right' method.
    """
    print(SEP)
    print("Test 'heavy_right'")
    print("(BST shown in level order)")
    print()
    test_bsts = (VALUES0, VALUES1, VALUES2,)

    for test_bst in test_bsts:
        source = to_BST(test_bst)
        print(f"source: {to_python_list(source)}")
        th = source.heavy_right()
        print("hr = source.heavy_right()")
        print(f"hr: {th}")
        print()


if __name__ == "__main__":
    print("BST_linked Testing")
    test_heavy_right()
