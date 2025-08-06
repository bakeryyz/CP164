"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-02-03"
-------------------------------------------------------
"""
# Imports

# Constants

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if x < 0 or y < 0:
        value = x - y
    else:
        value = recurse(x-1, y) + recurse(x, y-1)
    return value

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        value = n
    else:
        value = gcd(n, m % n)
    return value

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    if s == "":
        value = 0
    else:
        if s[0].lower() in "aeiou":
            value = 1 + vowel_count(s[1:])
        else:
            value = vowel_count(s[1:])

    return value

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        value = 1.0
    elif power < 0:
        value = 1.0 / to_power(base, -power)
    elif power % 2 == 0:
        value = to_power(base * base, power // 2)
    else:
        value = base * to_power(base, power - 1)

    return value

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    # Convert to lowercase and ignore non-letters
    s = ''.join(c for c in s if c.isalpha()).lower()

    if len(s) <= 1:
        value = True
    else:
        value = s[0] == s[-1] and is_palindrome(s[1:-1])
    return value

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    if not bag:
        value = []
    else:
        first = bag[0]
        rest = bag[1:]
        rest_set = bag_to_set(rest)
        if first not in rest_set:
            value = [first] + rest_set
        else:
            value = rest_set
    return value
