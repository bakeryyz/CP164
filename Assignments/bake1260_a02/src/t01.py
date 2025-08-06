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
# Imports
from Movie_utilities import get_by_year

class Movie:
    def __init__(self, title, year, genres, rating):
        self.title = title
        self.year = year
        self.genres = genres
        self.rating = rating

    def __repr__(self):
        return f"{self.title} ({self.year})"

def read_movies(file_path):
    movies = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) >= 4:
                title, year, genres, rating = parts[:4]
                movies.append(Movie(title, int(year), genres.split(', '), float(rating)))
    return movies

movies = read_movies("movie.txt")
year = int(input("Enter the year to list movies released: "))
ymovies = get_by_year(movies, year)
if ymovies:
    print(f"\nMovies released in {year}:")
    for movie in ymovies:
        print(movie)
else:
    print(f"\nNo movies found for the year {year}.")
