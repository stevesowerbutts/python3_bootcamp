# Tuple

Ordered collection or grouping of items - immutable (cant be changed)
eg. `numbers = (1,2,3,4)`

Faster than lists
Tuples can be used as valid keys in dictionary:
eg,
```
locations = {
    (35.675, 122.412): "Tokyo",
    (40.712, 74.006): "New York"
}
>>> locations[(35.675, 122.412)]
'Tokyo'
```

You cant use a list as a key in a dictionary, but you can use a tuple.
```
>>> locs = {[35.675, 122.412]: "Tokyo"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Some dict methods return tuples - this is because the key:values dont change.
```
>>> cats
{'name': 'red', 'Age': 13}
>>> cats.items()
dict_items([('name', 'red'), ('Age', 13)])
```


# Looping
For/While loops work in the same way.
```
for i in tuple:
    print(i)
```

# Methods

`count()` - returns the number of times a value is in a tuple
`index()` - returns the index at which a value is found in a tuple

# Nested tuples
Same as nested list
```
nums = (1,2,3,(4,5),6,7)
>>> nums[3]
(4, 5)
>>> nums[3][1]
5
```
Can also use slicing


# Set

Sets of unique unordered items, no duplicates
You cannot access items in a set by index (no order)
```
s = {1,2,3,4,4,4,4,'a'}
>>> s
{1, 2, 3, 4, 'a'}
>>> s[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable

>>> 4 in s
True
```
Sets are good for finding number of uniq items in a list:
```
>>> cities
['la', 'london', 'syd', 'melbs', 'syd', 'melbs']
>>> set(cities)
{'la', 'london', 'melbs', 'syd'}
>>> len(set(cities))
4
>>> list(set(cities))
['la', 'london', 'melbs', 'syd']
```

## Set methods

s.add() - adds item if it doesnt already exist
s.remove() - removes items if exists - *Key error if value is not found*
s.discard() - same as remove but no KeyErrors
s.copy() - duplicate of data but no identical in memory
s.clear() - empties set

## Set math

* Set union - generate a unique set from 2 sets
```
math_students = {'james','dave','emma','ros'}
bio_students = {'dave','rod','mik','ros'}

# Generate set of unique students
>>> math_students | bio_students
{'dave', 'rod', 'emma', 'james', 'ros', 'mik'}

# Generate set of students in both courses:
>>> math_students & bio_students
{'dave', 'ros'}
```

## Set comprehension
Similar to dict comprehension but without the key:value
```
>>> {x**2 for x in range(10)}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Change to Dictionary
>>> {x:x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```
Useful when converting other data types to a set
```
>>> string = "qwertyuiop"
>>> {char for char in string if char in 'aeiou'}
{'e', 'u', 'o', 'i'}
>>> len({char for char in string if char in 'aeiou'})
4
# Check whether string contains all vowels
>>> len({char for char in string if char in 'aeiou'}) == 5
False
```
