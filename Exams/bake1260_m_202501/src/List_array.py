"""
-------------------------------------------------------
Array version of the List ADT.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-02-08"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from copy import deepcopy


class List:
    """
    Implements an array-based List ADT.
    """

    def longest_run(self):
        """
        -------------------------------------------------------
        Returns the count of the largest number of adjacent values in source.
        Use: count = source.longest_run(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            count - the count of the largest number of adjacent values
                in source (int >= 0)
        -------------------------------------------------------
        """
        count = 0

        for i in range(1, len(self._values)):
            if self._values[i] == self._values[i - 1]:
                count += 1

        return count

    """
    DO NOT CHANGE CODE BELOW THIS LINE
    =======================================================================
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: source = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of source.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        self._values = self._values + [deepcopy(value)]
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
