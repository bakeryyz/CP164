"""
-------------------------------------------------------
Simple midterm testing.
Test calls are commented out at the bottom of the module in __main__ section.
Remove comment tag for any test you wish to execute.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-02-11"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from Stack_array import Stack
from functions_stack import check_parentheses

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40


def test_check_parentheses():
    print(SEP_FUNC)
    print("Test: check_parentheses")
    CASES = (
        "()", "(", ")", "(a)(b)", "(a(b)c)"
        )
    for case in CASES:
        print(SEP_TEST)
        print(f"checked = check_parentheses('{case}')")
        checked = check_parentheses(case)
        print(f"  checked: {checked}")


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_check_parentheses()
