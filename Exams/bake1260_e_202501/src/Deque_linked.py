"""
-------------------------------------------------------
Linked version of the Deque ADT.
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


class Deque:
    """
    Defines a linked Deque.
    """

    def is_mirror(self):
        """
        -------------------------------------------------------
        Determines if a Deque is mirrored, i.e. the left half
        and right half contain the same values in opposite order.
        Use: mirror = source.is_mirror()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            mirror - True if source is mirrored, False otherwise.
        -------------------------------------------------------
        """
        if self._count <= 1:
            return True
        
        left = self._front
        right = self._rear
        
        for _ in range(self._count // 2):
            if left._value != right._value:
                return False
            left = left._next
            right = right._prev
            
            return True


    def append_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of source.
        Use: source.append_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        if self._front is not None and self._front != self._rear:
            
            node = self._front
            self._front = self._front._next
            self._front._prev = None
            
            node._next = None
            node._prev = self._rear
            self._rear._next = node
            self._rear = node
            
            return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = Deque()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, self._front)

        if self._front is None:
            self._rear = node
        else:
            self._front._prev = node
        self._front = node
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, self._rear, None)

        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._count += 1
        return

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a Deque. l has taken the place of r,
        r has taken the place of l and _front and _rear are updated
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        if l is not r:
            # Swap the parameter node pointers - do not swap same node
            # l._prev, r._prev, l._next, r._next = r._prev, l._prev, r._next, l._next
            tmp = l._prev
            l._prev = r._prev
            r._prev = tmp

            tmp = r._next
            r._next = l._next
            l._next = tmp

            # FIX: If nodes are adjacent, previous swaps make nodes point to
            # themselves
            if l._prev is l:
                l._prev = r
            elif l._next is l:
                l._next = r

            if r._prev is r:
                r._prev = l
            elif r._next is r:
                r._next = l

            # Update nodes adjacent to l and r and front and/or rear as
            # necessary
            if l._prev is None:
                # l is the front
                self._front = l
            else:
                l._prev._next = l

            if l._next is None:
                # l is the rear
                self._rear = l
            else:
                l._next._prev = l

            if r._prev is None:
                # r is the front
                self._front = r
            else:
                r._prev._next = r

            if r._next is None:
                # r is the rear
                self._rear = r
            else:
                r._next._prev = r
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Deque_Node:
    """
    Defines a linked Deque node.
    """

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next
