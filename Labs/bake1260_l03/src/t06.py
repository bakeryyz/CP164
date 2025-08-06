"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-23"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

def parse_movies(file_name):
    movies = []
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            title = parts[0]
            year = int(parts[1])
            director = parts[2]
            rating = float(parts[3])
            genres = list(map(int, parts[4].split(","))) if parts[4] else []
            movies.append((title, year, director, rating, genres))
    return movies


def test_priority_queue(movies):
    pq = Priority_Queue()
    for movie in movies:
        title, _, _, rating, _ = movie
        pq.insert((title, rating))
    print("Highest priority movie:", pq.peek())
    print("\nMovies removed in priority order (by rating):")
    while not pq.is_empty():
        print(pq.remove())


if __name__ == "__main__":
    movies = parse_movies("movies.txt")
    test_priority_queue(movies)
