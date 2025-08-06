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
from Movie_utilities import genre_counts

class Movie:
    def __init__(self, title, year, genres, rating):
        self.title = title
        self.year = year
        self.genres = genres
        self.rating = rating

    def __repr__(self):
        return f"{self.title} ({', '.join(self.genres)})"

def read_movies(file_path):
    with open(file_path, 'r') as file:
        return [Movie(*line.strip().split('|')[:2], line.strip().split('|')[2].split(', '), float(line.strip().split('|')[3])) for line in file]

GENRE_CODES = [
    "Action", "Comedy", "Drama", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", "Crime"
]

movies = read_movies("movie.txt")
counts = genre_counts(movies)

print("\nGenre Counts:")
for genre, count in zip(GENRE_CODES, counts):
    print(f"{genre}: {count}")

