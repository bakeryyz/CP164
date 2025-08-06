"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-04-16"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Queue:
    """
    A linked Queue class.
    """

    def remove_value(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the Queue that match key.
        Use: source.remove_value(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            None
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        
        while current is not None:
            if current._value == key:
                if previous is None:
                    self._front = current._next
                else:
                    previous._next = current._next
                    
                if current == self._rear:
                    self._rear = previous

                self._count -= 1
            else:
                previous = current

            current = current._next

        return
    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        ---------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        ---------------------------------------------------------
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            a new Queue object (Queue)
        ---------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            None
        -------------------------------------------------------
        """
        node = _Queue_Node(value)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Queue_Node:
    """
    A linked Queue Node class.
    """

    def __init__(self, value):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to None since it must be added to the rear
        of the queue.
        Use: node = _Queue_Node(value)
        ---------------------------------------------------------
        Parameters:
            value - value for node (?)
        Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = None
