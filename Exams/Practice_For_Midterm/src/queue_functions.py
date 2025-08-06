"""
-------------------------------------------------------
 Queue Functions
-------------------------------------------------------

-------------------------------------------------------
"""


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source. When finished, values
    in source are rotated n positions to the right.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌​‌​​‌‌‌‌‌​‌​‌‌​​:
        None
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
