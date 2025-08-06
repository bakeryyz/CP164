"""
-------------------------------------------------------
Queue Functions
-------------------------------------------------------
Author: Ben Baker
ID:     169081260
Email:  bake1260@mylaurier.ca
__updated__ = "2025-02-06"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from Queue_array import Queue


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source, meaning moving its contents
    from the front to the rear n times.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌‌‌‌‌‌​​‌‌​‌​‌‌​​:
        None
    -------------------------------------------------------
    Examples:
        source: [0, 1, 2, 3, 4, 5], queue_rotate(source, 3), source: [3, 4, 5, 0, 1, 2]
        source: [0, 1, 2, 3, 4, 5], queue_rotate(source, -1), source: [5, 0, 1, 2, 3, 4]
    -------------------------------------------------------
    """
    source_list = []

    for i in range(len(source)):
        source_list.append(source.remove())

    temp = source_list

    for i in range(len(source_list)):
        new_index = (i + n) % len(source_list)
        temp[new_index] = i

    for i in range(len(temp)):
        source.insert(temp[i])

    return
