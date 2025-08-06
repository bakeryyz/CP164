"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-15"
-------------------------------------------------------
"""
from Movie_utilities import get_by_rating

class Movie:
    def __init__(self, title, year, genres, rating):
        self.title = title
        self.year = year
        self.genres = genres
        self.rating = rating

    def __repr__(self):
        return f"{self.title} ({self.rating})"

def read_movies(file_path):
    with open(file_path, 'r') as file:
        return [
            Movie(*line.strip().split('|')[:2], line.strip().split('|')[2].split(', '), float(line.strip().split('|')[3]))
            for line in file
            if len(line.strip().split('|')) >= 4
        ]

movies = read_movies("movie.txt")
min_rating = float(input("Enter the minimum rating to list movies: "))
rmovies = get_by_rating(movies, min_rating)
print(f"\nMovies with a rating >= {min_rating}:")
print("\n".join(str(movie) for movie in rmovies) if rmovies else f"No movies found with a rating >= {min_rating}.")
