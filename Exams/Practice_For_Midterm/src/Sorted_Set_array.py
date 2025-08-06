"""
-------------------------------------------------------
Array version of the Sorted_Set ADT.
-------------------------------------------------------

-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            a new Sorted_Set object. (Sorted_Set)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._values == []

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            the number of values in source. (int)
        -------------------------------------------------------
        """

        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in self.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            i - the index of the only occurrence of key in
                self, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        low = 0
        high = len(self._values) - 1

        while low < high:
            mid = (high - low) // 2 + low

            if key > self._values[mid]:
                low = mid + 1
            else:
                high = mid

        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1

        return i

    def add(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, adds a copy of value
        to source. Returns True if value is added, False otherwise.
        Values in source must remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            added - True if value added to source, False otherwise. (bool)
        -------------------------------------------------------
        """
        added = True

        if value not in self._values:
            low = 0
            high = len(self._values) - 1

            while low <= high:
                mid = (high - low) // 2 + low

                if value < self._values[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            self._values.insert(low, value)
        else:
            added = False

        return added

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - data key (*)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """
        i = self._binary_search(key)

        if i != -1:
            value = self._values.pop(i)
        else:
            value = None

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - data key. (*)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            True if source contains key, False otherwise. (bool)
        -------------------------------------------------------
        """

        return self._binary_search(key) != -1

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether source == target are equivalent.
        Values in source and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Sorted_Set to compare against (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            equals - True if source contains the same values as target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """
        equals = True

        if self._values != target._values:
            equals = False

        return equals

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Tests whether every value in source is also in target.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            subset - True if all values in source are also in target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({0,1,2,3,4}): True
            {1,2,3}.issubset({1,2,4,5}): False
        -------------------------------------------------------
        """
        i = 0
        subset = True

        while i < len(self._values) and subset == True:
            if self._values[i] not in target._values:
                subset = False
            i += 1

        return subset

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sorted_Sets are disjoint if and only if their intersection
        is the empty Sorted_Set.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            disjoint - True if source has no values in common with target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        disjoint = True

        for i in range(len(self._values)):
            if self._values[i] in target._values:
                disjoint = False

        return disjoint

    def intersection(self, source2):
        """
        -------------------------------------------------------
        Return target with copies of values common to source1 and source2.
        Values may appear only once in target. Values must be sorted.
        Use: target = source1.intersection(source2)
        -------------------------------------------------------
        Parameters:
            source2 - an array-based Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            target - the intersection of source1 and source2. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({3,4,5}): {3}
            {1,2,3}.intersection({4,5,6}): {}
        -------------------------------------------------------
        """
        target = Sorted_Set()

        for i in range(len(self._values)):
            if (self._values[i] not in target._values) and (self._values[i] in source2._values):
                target._values.append(self._values[i])

        return target

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
            value - the next value in the Sorted_Set. (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
