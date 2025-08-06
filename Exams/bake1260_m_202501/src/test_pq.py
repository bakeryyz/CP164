"""
-------------------------------------------------------
Simple midterm testing.
Test calls are commented out at the bottom of the module in __main__ section.
Remove comment tag for any test you wish to execute.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-02-06"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from Priority_Queue_array import Priority_Queue
from functions_pq import pq_triage

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40


def print_values(name, source):
    """
    Prints data structure _values formatted as 'name: [source._values contents]'
    """
    print(f"{name}: [", end='')
    for v in source:
        print(f"{v}, ", end="")
    print("]")
    return


def fill_pq(values):
    """
    Returns a Priority_Queue containing values
    """
    source = Priority_Queue()
    for v in values:
        source.insert(v)
    return source


def test_pq_triage():
    print(SEP_FUNC)
    print("Test: pq_triage")
    values = [4, 6, 2, 3, 9, 7]
    CASES = (1, 8, 4)

    for key in CASES:
        print(SEP_TEST)
        source = fill_pq(values)
        print_values("source", source)
        pq_triage(source, key)
        print(f"pq_triage(source, {key})")
        print_values("result", source)


def test_triage():
    print(SEP_FUNC)
    print("Test: triage")
    values = [4, 6, 2, 3, 9, 7]
    CASES = (1, 8, 4)

    for key in CASES:
        print(SEP_TEST)
        source = fill_pq(values)
        print_values("source", source)
        source.triage(key)
        print(f"source.triage({key})")
        print_values("result", source)


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_pq_triage()
    test_triage()
