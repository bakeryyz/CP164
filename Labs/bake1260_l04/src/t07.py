"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-30"
-------------------------------------------------------
"""
from List_array import List

def array_to_list(llist, source):
    while len(source) > 0:
        llist.append(source.pop(0))
    return None

def list_to_array(llist, target):
    while len(llist) > 0:
        target.append(llist.pop(0))
    return None

def list_test(source):
    lst = List()

    for item in source:
        lst.append(item)
    lst.pop(0)
    lst.insert(0, source[0])
    print("Max:", lst.max())
    print("Min:", lst.min())
    lst.remove(source[1])
    print("Index:", lst.index(source[2]))
    print("Value:", lst[2])
    lst[2] = source[3]
    target = []
    list_to_array(lst, target)
    array_to_list(lst, target)
    print("Find:", lst.find(source[2]))
    print("Count:", lst.count(source[2]))

movie_data = []

with open('movie.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('|')
        movie = parts[0]
        year = int(parts[1])
        director = parts[2]
        rating = float(parts[3])
        ratings = list(map(int, parts[4].split(',')))
        movie_data.append((movie, year, director, rating, ratings))

list_test(movie_data)
