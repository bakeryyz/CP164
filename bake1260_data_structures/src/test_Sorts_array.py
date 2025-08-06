"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-20"
-------------------------------------------------------
"""

# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = [Number(i) for i in range(SIZE)]
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = [Number(i) for i in range(SIZE-1, -1, -1)]
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = []
    for i in range(TESTS):
        array = [Number(random.randint(0, XRANGE)) for j in range(SIZE)]
        arrays.append(array)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Sorts.swaps = 0
    Number.comparisons = 0
    sorted_arr = create_sorted()
    reversed_arr = create_reversed()
    random_arrs = create_randoms()

    func(sorted_arr)
    sorted_swaps = Sorts.swaps
    sorted_comparisons = Number.comparisons

    Sorts.swaps = 0
    Number.comparisons = 0

    func(reversed_arr)
    reverse_comparisons = Number.comparisons
    reverse_swaps = Sorts.swaps

    Sorts.swaps = 0
    Number.comparisons = 0

    for arr in random_arrs:
        func(arr)

    random_swaps = Sorts.swaps / TESTS
    random_comparisons = Number.comparisons / TESTS

    Sorts.swaps = 0
    Number.comparisons = 0

    # Print results
    print(f"{title:14s} {sorted_comparisons:8d} {reverse_comparisons:8d} {random_comparisons:>8.0f} {sorted_swaps:8.0f} {reverse_swaps:8.0f} {random_swaps:>8.0f}")
