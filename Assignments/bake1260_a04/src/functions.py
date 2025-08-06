"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-28"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

# Constants


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    while source1.is_empty() is False and source2.is_empty() is False:
        target.insert(source1.remove())
        target.insert(source2.remove())
    while source1.is_empty() is False:
        target.insert(source1.remove())
    while source2.is_empty() is False:
        target.insert(source2.remove())
    return target
