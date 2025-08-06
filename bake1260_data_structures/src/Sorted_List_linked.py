"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-06-10"
-------------------------------------------------------
"""
from copy import deepcopy

class _SL_Node:
    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_

class Sorted_List:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        previous, current, _ = self._linear_search(value)
        new_node = _SL_Node(value, None)
        if previous is None:
            new_node._next = self._front
            self._front = new_node
            if self._rear is None:
                self._rear = new_node
        else:
            new_node._next = current
            previous._next = new_node
            if current is None:
                self._rear = new_node
        self._count += 1

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
        
        while current is not None and current._value < key:
            previous = current
            current = current._next
            index += 1
            
        if current is None or (current is not None and current._value > key):
            index = -1
            
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, _ = self._linear_search(key)
        value = None
        
        if current is not None and current._value == key:
            value = current._value
            if previous is None:
                self._front = current._next
            else:
                previous._next = current._next
            if current._next is None:
                self._rear = previous
            self._count -= 1
            
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        if self._front is None:
            self._rear = None
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        while self.remove(key) is not None:
            pass

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        return deepcopy(current._value) if current is not None and current._value == key else None

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, current, index = self._linear_search(key)
        return index if current is not None and current._value == key else -1

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        return -self._count <= i < self._count

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = self._count + i
        current = self._front
        for _ in range(i):
            current = current._next
        return deepcopy(current._value)

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        return current is not None and current._value == key

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        return deepcopy(self._rear._value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        return deepcopy(self._front._value)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        occurrences = 0
        
        while current is not None and current._value == key:
            occurrences += 1
            current = current._next
            
        return occurrences

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            return
        current = self._front
        while current._next is not None:
            if current._value == current._next._value:
                current._next = current._next._next
                self._count -= 1
            else:
                current = current._next
        self._rear = current

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"
        previous = None
        current = self._front
        if len(args) == 1:
            i = args[0]
            if i < 0:
                i = self._count + i
            j = 0
            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            while current._next is not None:
                previous = current
                current = current._next
        value = current._value
        if previous is None:
            self._front = current._next
        else:
            previous._next = current._next
        if current._next is None:
            self._rear = previous
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        curr1 = source1._front
        curr2 = source2._front
        while curr1 is not None and curr2 is not None:
            if curr1._value < curr2._value:
                curr1 = curr1._next
            elif curr1._value > curr2._value:
                curr2 = curr2._next
            else:
                self.insert(curr1._value)
                curr1 = curr1._next
                curr2 = curr2._next
                self.clean()

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        curr1 = source1._front
        curr2 = source2._front
        while curr1 is not None or curr2 is not None:
            if curr2 is None or (curr1 is not None and curr1._value < curr2._value):
                self.insert(curr1._value)
                curr1 = curr1._next
            elif curr1 is None or (curr2 is not None and curr2._value < curr1._value):
                self.insert(curr2._value)
                curr2 = curr2._next
            else:
                self.insert(curr1._value)
                curr1 = curr1._next
                curr2 = curr2._next
        self.clean()

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        
        curr1 = source1._front
        curr2 = source2._front
        previous = None
        
        # Interlace nodes from both lists while maintaining sorted order
        while curr1 is not None or curr2 is not None:
            if curr2 is None or (curr1 is not None and curr1._value <= curr2._value):
                # Take node from source1
                current = curr1
                curr1 = curr1._next
            else:
                # Take node from source2
                current = curr2
                curr2 = curr2._next
                
            # Link the node
            if previous is None:
                self._front = current
            else:
                previous._next = current
            previous = current
            self._count += 1
        
        # Ensure the last node's next pointer is None
        if previous is not None:
            previous._next = None
            self._rear = previous
            
        # Empty the source lists
        source1._front = None
        source1._rear = None
        source1._count = 0
        source2._front = None
        source2._rear = None
        source2._count = 0

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a sorted list (Sorted_List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equal = True
        if self._count != target._count:
            equal = False
        else:
            current1 = self._front
            current2 = target._front
            while current1 is not None and equal:
                if current1._value != current2._value:
                    equal = False
                current1 = current1._next
                current2 = current2._next
        return equal

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front
        while current is not None:
            yield current._value
            current = current._next