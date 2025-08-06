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
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, prev_, next_):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, prev_, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            prev_ - another deque node (_Deque_Node)
            next_ - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = prev_
        self._next = next_


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
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
        Returns:
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
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equal = True
        
        if self._count != target._count:
            equal = False
        else:
            current_self = self._front
            current_target = target._front
            
            while current_self is not None and equal:
                if current_self._value != current_target._value:
                    equal = False
                current_self = current_self._next
                current_target = current_target._next
                
        return equal

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Deque_Node(value, None, self._front)
        
        if self._front is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._front._prev = new_node
            self._front = new_node
            
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
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Deque_Node(value, self._rear, None)
        
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
            
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        
        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        
        if self._front is None:
            self._rear = None
        else:
            self._front._prev = None
            
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        value = self._rear._value
        self._rear = self._rear._prev
        self._count -= 1
        
        if self._rear is None:
            self._front = None
        else:
            self._rear._next = None
            
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        return deepcopy(self._front._value)

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        return deepcopy(self._rear._value)

    def _swap(self, left, right):
        """
        -------------------------------------------------------
        Swaps two nodes in the deque by adjusting their links.
        Use: deque._swap(left, right)
        -------------------------------------------------------
        Parameters:
            left - a deque node (_Deque_Node)
            right - a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert left is not None and right is not None, "Cannot swap None nodes"

        if left is right:
            done = True
        else:
            done = False
            if left._next is right:
                left_prev = left._prev
                right_next = right._next
                
                if left_prev is not None:
                    left_prev._next = right
                if right_next is not None:
                    right_next._prev = left
                
                right._prev = left_prev
                right._next = left
                left._prev = right
                left._next = right_next
                
                if self._front is left:
                    self._front = right
                if self._rear is right:
                    self._rear = left
                    
            elif right._next is left:
                self._swap(right, left)
                
            else:
                left_prev = left._prev
                left_next = left._next
                right_prev = right._prev
                right_next = right._next
                
                if left_prev is not None:
                    left_prev._next = right
                if left_next is not None:
                    left_next._prev = right
                if right_prev is not None:
                    right_prev._next = left
                if right_next is not None:
                    right_next._prev = left
                
                right._prev = left_prev
                right._next = left_next
                left._prev = right_prev
                left._next = right_next
                
                if self._front is left:
                    self._front = right
                elif self._front is right:
                    self._front = left
                if self._rear is left:
                    self._rear = right
                elif self._rear is right:
                    self._rear = left
                    
        return