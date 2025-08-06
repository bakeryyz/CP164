"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-02-25"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to None since it must be added to the rear
        of the queue.
        Use: node = _Queue_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = None


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
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
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Queue_Node(value)
        
        if self._front is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        
        if self._front is None:
            self._rear = None
            
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        return deepcopy(self._front._value)

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        node = source._front
        source._front = source._front._next
        source._count -= 1
        
        if source._front is None:
            source._rear = None
            
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
        node._next = None
        self._count += 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        if self._front is None:
            self._front = source._front
        else:
            self._rear._next = source._front
            
        self._rear = source._rear
        self._count += source._count
        
        source._front = None
        source._rear = None
        source._count = 0
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while not (source1.is_empty() and source2.is_empty()):
            if not source1.is_empty():
                self._move_front_to_rear(source1)
            if not source2.is_empty():
                self._move_front_to_rear(source2)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into two alternating queues.
        Values are taken alternately from source to target1 and target2.
        Source becomes empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        
        while self._front is not None:
            if self._front is not None:
                target1._move_front_to_rear(self)
            if self._front is not None:
                target2._move_front_to_rear(self)
                
        return target1, target2

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this queue against another queue for equality.
        Values are compared in order from front to rear.
        Use: source1 == source2
        -------------------------------------------------------
        Parameters:
            other - another queue to compare to (Queue)
        Returns:
            True if queues are equal, False otherwise
        -------------------------------------------------------
        """
        equal = True
        
        if self._count != other._count:
            equal = False
        else:
            current1 = self._front
            current2 = other._front
            
            while current1 is not None and equal:
                if current1._value != current2._value:
                    equal = False
                current1 = current1._next
                current2 = current2._next
                
        return equal
