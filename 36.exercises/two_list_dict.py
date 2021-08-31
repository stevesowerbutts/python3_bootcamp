import itertools

def two_list_dictionary(list1, list2):
    '''
    Create a dictionary from two lists of varying lengths
    First list containts keys, second list contains values
    Returns a dictionary, with keys returning None if there arent enough values

    Used the below for info on using itertools:
    https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length
    '''
    new_dict = {k:v for k,v in itertools.zip_longest(list1, list2) if k}
    return new_dict

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}
