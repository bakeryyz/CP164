"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-12"
-------------------------------------------------------
"""
import unittest
from BST_linked import BST  # Assuming you have a BST implementation
from Letter import Letter
from functions import do_comparisons

class TestDoComparisons(unittest.TestCase):
    
    def setUp(self):
        """ Sets up the BST with all letters of the alphabet """
        self.bst = BST()
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.bst.insert(Letter(letter))
    
    def test_do_comparisons(self):
        """ Tests do_comparisons by processing a sample text file """
        with open("sample_text.txt", "r", encoding="utf-8") as file:
            do_comparisons(file, self.bst)
        
        total_comparisons = sum(node.comparisons for node in self.bst.inorder())
        self.assertGreater(total_comparisons, 0, "Total comparisons should be greater than 0")

if __name__ == "__main__":
    unittest.main()