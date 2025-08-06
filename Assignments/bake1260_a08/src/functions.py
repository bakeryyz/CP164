"""
-------------------------------------------------------
Functions to process files and analyze comparisons in a BST.
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-12"
-------------------------------------------------------
"""
from Letter import Letter


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # Read file and process each character
    for line in file_variable:
        for char in line:
            if char.isalpha():  # Process only alphabetic characters
                letter = Letter(char.upper())
                bst.retrieve(letter)  # Triggers comparisons in BST


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    for node in bst.inorder():  # Perform inorder traversal
        total += node.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total_count = sum(node.count for node in bst.inorder())
    
    print("\nLetter Count/Percent Table\n")
    print(f"Total Count: {total_count:,}")
    print("\nLetter  Count       %")
    print("---------------------")
    
    for node in bst.inorder():
        percentage = (node.count / total_count) * 100 if total_count > 0 else 0
        print(f"    {node.letter}  {node.count:6,}   {percentage:5.2f}%")

