"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-11"
-------------------------------------------------------
"""

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
     1652346    3 Dark City, 1998
      848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """

    table = {i: [] for i in range(slots)}

    for num in values:
        hash_num = hash(num) % slots
        table[hash_num].append(num)

    print("Hash     Slot Key")
    print("-------- ---- --------------------")

    for slot, values in table.items():
        for num in values:
            hash_num = hash(num)
            key = str(num)

            print(f"{hash_num:8} {slot:4} {key}")

    return
