# coding: utf-8
"""
-------------------------------------------------------
Linked version of the List ADT.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-03-28"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class List:
    """
    A linked List class.
    """

    def split_alt_many(self, n):
        """
        -------------------------------------------------------
        Splits the source List into n separate target Lists with values
        alternating into the targets. At finish source List is empty.
        Order of source values is preserved.
        Always produces n Lists, even if len(source) < n.
        Use: targets = source.split_alt_many(n)
        -------------------------------------------------------
        Parameters:
            n - number of target Lists (int > 0)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            targets - Python list containing n Lists (list of Lists)
        -------------------------------------------------------
        """
        targets = [List() for _ in range(n)]
        
        current = self._front
        index = 0 
        
        while current is not None:
            target_list = targets[index]
            if target_list._front is None:
                target_list._front = current
            else:
                target_list._rear._next = current
                
            target_list._rear = current
            current = current._next
            target_list._rear._next = None
            target_list._count += 1
            index = (index + 1) % n
            
            self._front = None
            self._rear = None
            self._count = 0
            
            return targets


    def replace_many(self, key, value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in source with value.
        List is otherwise unchanged.
        Use: source.replace_many(key, value)
        -------------------------------------------------------
        Parameters:
            key - a key that may be in source (?)
            value - the replacement for key (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None.
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            if current._value == key:
                current._value = value
            current = current._next

        return
    
    def common_node(self, target):
        """
        -------------------------------------------------------
        Finds the first node common to two Lists.
        Use: common = source.common_node(target)
        -------------------------------------------------------
        Parameters:
            target - List to search for first common node (List)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            common - the first node common to source and target,
                None if source and target have no common nodes (_List_Node)
        -------------------------------------------------------
        """
        current = self._front
        source_nodes = set()
        
        while current is not None:
            source_nodes.add(current)
            current = current._next
            
            current = target._front
            while current is not None:
                if current in source_nodes:
                    return current
                current = current._next
                
                return None  
            
    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
