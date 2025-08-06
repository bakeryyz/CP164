"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
Section: CP164 C
__updated__ = "2025-01-06"
-------------------------------------------------------
"""
# Imports
import Movie_utilities

# Constants
with open("movie.txt", "r") as file:
    line = file.readline().strip()
    while line != "":
        print(line)
        movie = Movie_utilities.read_movie(line)
        print(movie)
        print()
        line = file.readline().strip()
