"""
-------------------------------------------------------
Linked version of the List ADT.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2024-11-26"
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

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """

        target1 = List()
        target2 = List()
        add_to_target1 = True

        while self._front is not None:
            current_node = self._front
            self._front = self._front._next
            current_node._next = None

            if add_to_target1:
                if target1._front is None:
                    target1._front = current_node
                    target1._rear = current_node
                else:
                    target1._rear._next = current_node
                    target1._rear = current_node
                
                target1._count += 1
            else:
                if target2._front is None:
                    target2._front = current_node
                    target2._rear = current_node
                else:
                    target2._rear._next = current_node
                    target2._rear = current_node
                
                target2._count += 1
            
            add_to_target1 = not add_to_target1

            self._rear = None
            self._count = 0

        return target1, target2

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """

        # Check if pln and prn are the same node
        if pln is prn:
            return 
        
        # Both None
        if pln is None:
            ln = self._front
        else:
            ln = pln._next

        if prn is None:
            rn = self._front
        else:
            rn = prn._next

        # if either node is None
        if ln is None or rn is None:
            return 
        
        if ln is rn:
            return
        
        # swap the nodes
        if ln._next is rn:
            ln._next = rn._next
            rn._next = ln
            if pln is None:
                self._front = rn
            else:
                pln._next = rn

        elif rn._next is ln:
            rn._next = ln._next
            ln._next = rn

            if prn is None:
                self._front = ln
            else:
                prn._next = ln

        else:
            temp_ln_next = ln._next
            temp_rn_next = rn._next

            if pln is None:
                self._front = rn
            else:
                pln._next = rn

            if prn is None:
                self._front = ln
            else:
                prn._next = ln

            ln._next = temp_rn_next
            rn._next = temp_ln_next


        if self._rear is ln:
            self._rear = rn
        elif self._rear is rn:
            self._rear = ln


        if ln._next is None:
            self._rear = ln
        if rn._next is None:
            self._rear = rn


        if self._count == 1:
            self._rear = self._front
        elif self._count == 0:
            self._front = None
            self._rear = None

        return
    
    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
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
        Returns:
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
        Returns:
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
        Returns:
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
        Returns:
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
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
