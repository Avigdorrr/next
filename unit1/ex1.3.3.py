def is_funny(string):
    return all([False if char != 'h' and char != 'a' else True for char in string])
