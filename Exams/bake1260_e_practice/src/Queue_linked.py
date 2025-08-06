"""
-------------------------------------------------------
Linked version of the Queue ADT.
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


class Queue:
    """
    A linked Queue class.
    """

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # your code here

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
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        node = _Queue_Node(value, None)

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

    def __init__(self, value, next_):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        ---------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns‌​‌‌‌‌‌‌‌​‌​‌​​​‌‌‌​‌‌‌‌‌‌​​:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
