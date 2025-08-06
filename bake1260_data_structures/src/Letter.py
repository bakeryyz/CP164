"""
-------------------------------------------------------
Stores a single letter of the alphabet, and counts occurrences and
comparisons when the letter is used.
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-03-12"
-------------------------------------------------------
"""

class Letter:
    def __init__(self, letter):
        """
        -------------------------------------------------------
        Initialize a Letter object.
        Use: l = Letter(char)
        -------------------------------------------------------
        Parameters:
            letter - a single uppercase letter of the alphabet (str)
        Returns:
            A new Letter object (Letter)
        -------------------------------------------------------
        """
        assert letter.isalpha() and letter.isupper(), "Invalid letter"
        
        self.letter = letter
        self.count = 0  # Tracks occurrences of this letter being retrieved
        self.comparisons = 0  # Counts comparisons made when searching for this letter

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Letter data.
        Use: print(m)
        Use: s = str(m)
        -------------------------------------------------------
        Returns:
            The values of self.letter, self.count, and self.comparisons (str)
        -------------------------------------------------------
        """
        return f"{self.letter}: {self.count}, {self.comparisons}"

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this Letter against another Letter for equality.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if the letters match, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        return self.letter == target.letter

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Letter comes before another in the alphabet.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if source precedes target, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        return self.letter < target.letter

    def __gt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Letter follows another in the alphabet.
        Use: source > target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if source follows target, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        return self.letter > target.letter

