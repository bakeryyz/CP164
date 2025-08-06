"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from List_array import List

# Constants

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        x = source.pop()
        stack.push(x)
        
    return None
    
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    
    return None

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    array_to_stack(stack, source)  # Fill stack from source

    print("Is the stack empty?", stack.is_empty())
    print("Pushing 5:", stack.push(5))
    print("Popping 5:", stack.pop())
    print("Peek:", stack.peek())

    return None

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        queue.insert(source.pop(0))
        
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print(q.is_empty())
    for value in a:
        q.insert(value)
    print(q.is_empty())
    print(q.peek())
    while not q.is_empty():
        print(q.remove())
    print(q.is_empty())
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print(pq.is_empty())
    for value in a:
        pq.insert(value)
    print(pq.is_empty())
    print(pq.peek())
    while not pq.is_empty():
        print(pq.remove())
    print(pq.is_empty())
    
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contents of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))

    return None


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))

    return None


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # Tests for the List methods go here

    print("List is empty:", lst.is_empty())

    print("\nAppending data to the list:")
    for item in source:
        print(item)
        lst.append(item)
    print("List is empty:", lst.is_empty())
    print("List length:", len(lst))
    print("List:", lst)

    print("\nRemoving an element from the list:")
    lst.pop(0)
    print("List:", lst)

    print("\nInserting an element into the list:")
    lst.insert(0, source[0])
    print("List:", lst)

    print("\nFinding the maximum value in the list:")
    print("Max:", lst.max())

    print("\nFinding the minimum value in the list:")
    print("Min:", lst.min())

    print("\nRemoving a value from the list:")
    lst.remove(source[1])
    print("List:", lst)

    print("\nIndex of the first occurrence of a value:")
    print("Index:", lst.index(source[2]))

    print("\nGetting an element at a specific index:")
    print("Value:", lst[2])

    print("\nSetting the value of an element at a specific index:")
    lst[2] = source[3]
    print("List:", lst)

    target = []
    print("\nConverting the list to an array:")
    list_to_array(lst, target)
    print("Array:", target)

    print("\nConverting the array back to a List:")
    array_to_list(lst, target)
    print("List:", lst)

    print("\nFinding an element in the list:")
    print("Find:", lst.find(source[2]))

    print("\nCounting occurrences of a value in the list:")
    print("Count:", lst.count(source[2]))

    return

