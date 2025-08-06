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

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.genre})"

from Stack_array import Stack

def stack_test():
    stack = Stack()
    for line in open('movies.txt'):
        stack.push(Movie(*line.strip().split(',')))
    
    print(stack.pop(), stack.peek())

if __name__ == "__main__":
    stack_test()

