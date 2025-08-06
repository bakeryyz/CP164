"""
-------------------------------------------------------
Exam: Simple BST testing

See main code at bottom
Remove '#' from lines to test
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2024-11-26"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
VALUES0 = (11, 7, 6, 9, 8, 15, 12, 18,)
VALUES1 = (2, 3, 1,)
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


def test_node_counts():
    """
    Tests the 'node_counts' method.
    """
    print(SEP)
    print("Test 'node_counts'")
    print("(BST shown in level order)")
    print()

    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    zero, one, two = source.node_counts()
    print("zero, one, two = source.node_counts()")
    print(f"zero: {zero}, one: {one}, two: {two}")
    print()


def test_is_valid():
    """
    Tests the 'is_valid' method.
    """
    print(SEP)
    print("Test 'is_valid'")
    print("(BST shown in level order)")
    print()
    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    valid = source.is_valid()
    print("valid = source.is_valid()")
    print(f"valid: {valid}")
    print()
    hold = source._root._value
    source._root._value = 99
    print(f"source: {to_python_list(source)}")
    valid = source.is_valid()
    print("valid = source.is_valid()")
    print(f"valid: {valid}")
    print()
    source._root._value = 0
    print(f"source: {to_python_list(source)}")
    valid = source.is_valid()
    print("valid = source.is_valid()")
    print(f"valid: {valid}")
    print()
    # return root to original value
    source._root._value = hold
    # swap left and right children
    temp = source._root._left._value
    source._root._left._value = source._root._right._value
    source._root._right._value = temp
    print(f"source: {to_python_list(source)}")
    valid = source.is_valid()
    print("valid = source.is_valid()")
    print(f"valid: {valid}")
    print()
    # swap left and right children back
    temp = source._root._left._value
    source._root._left._value = source._root._right._value
    source._root._right._value = temp
    # make grandchild wrong
    source._root._left._right._value = 99
    print(f"source: {to_python_list(source)}")
    valid = source.is_valid()
    print("valid = source.is_valid()")
    print(f"valid: {valid}")
    print()


if __name__ == "__main__":
    """
    Remove Comment '#' from function calls to test
    """
    print("BST_linked Testing")
    test_node_counts()
    # test_is_valid()
