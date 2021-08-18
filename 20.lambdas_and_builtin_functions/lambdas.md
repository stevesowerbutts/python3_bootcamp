# Lambdas & built in functions


Like a function, but a single line, unlike a function it has no name (Also known as an anonymous function)

Not that common, can save them as variables, but that is also not common

add_values = lambda x, y: x + y
multiply_values = lambda x, y: x * y



# Map

Standard function, excepts at least 2 objects, a function and an iterable object (lists,strings, sets, dictionaries, tuples)
Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

```
l = [1,2,3,4]
doubles = list(map(lambda x: x*2, l))
doubles # [2,4,6,8]
```

```
names = [
  {'first': 'Rusty', 'last': 'Steele'},
  {'first': 'Colt', 'last': 'Steele'},
  {'first': 'Blue', 'last': 'Steele'},
]

first_names = list(map(lambda x: x['first'], names))
first_names # ['Rusty', 'Colt', 'Blue']
```

# Filter
Lambda for each value in the iterable
returns a filter object which can be converted into other iterables
The object contains only the values that return true to the lambda

```
l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
evens # [2,4]
```

# Combining filter and map
filter applies first and passes values to map
syntax is list(map(lambda to run on filtered values, filter(lambda to filter original values)))

```
names = ['lassie', 'Colt', 'Rusty']

list(map(lambda name: f"Your instructor name is {name}",
      filter(lambda value: len(value) < 5, names)))
# ['Your instructor name is Colt']
```

**In the above scenario you should use list comprehensions**
The above would look like:
`[f'Your instructor name is {name}' for name in names if len(name) < 5]`

# all
Returns Trus if all iterable valus are truthy (or if the iterable is empty)
```
>>> nums = [0,2,4,6]
>>> all([num % 2 == 0 for num in nums])
True
>>> nums = [0,2,4,6,7]
>>> all([num % 2 == 0 for num in nums])
False
```

# any
Return True if any element of the iterable list is truthy.
Returns false if the iterable is empty.
```
>>> nums = [0,2,4,6,7]
>>> any([num % 2 == 0 for num in nums])
True
>>> nums = [1,3,5,7]
>>> any([num % 2 == 0 for num in nums])
False
```

**For both all and any you can use a generator expression `()` rather than list comprehensions `[]`**
generator expressions are used when you do not need to store the generated list of results.
ie. for all/any you are only checking if the value is true or false, so could write:
```
>>> nums = [0,2,4,6,7]
>>> (num % 2 == 0 for num in nums)
<generator object <genexpr> at 0x102c4dba0>

>>> any(num % 2 == 0 for num in nums)
True
>>> nums = [1,3,5,7]
>>> any(num % 2 == 0 for num in nums)
False
```
Basically use generator expressions if you are only iterating once.
If you want to store and use the generated results, then use list comprehensions.


# sorted (different to list.sort)

Sorted list from items in an iterable
  - accepts tuples,lists,dicts etc
  - returns a sorted list
*Doesnt change the original variables, unlike list.sort()*
```
>>> nums = [1,54,6,4,646,2]
>>> sorted(nums)
[1, 2, 4, 6, 54, 646]
>>> nums
[1, 54, 6, 4, 646, 2]
>>> nums.sort()
>>> nums
[1, 2, 4, 6, 54, 646]
>>> sorted(nums,reverse=True)
[646, 54, 6, 4, 2, 1]
```
- for lists of dicts you have to specify the key to sort by.
```
users = [
  {'user': 'tob', 'colour': 'blue'},
  {'user': 'xavier', 'colour': 'green'},
  {'user': 'cob', 'colour': 'red'}
]

>>> sorted(users, key=lambda user: user['user'])
[{'user': 'cob', 'colour': 'red'}, {'user': 'tob', 'colour': 'blue'}, {'user': 'xavier', 'colour': 'green'}]

>>> sorted(users, key=lambda user: len(user['colour']))
[{'user': 'cob', 'colour': 'red'}, {'user': 'tob', 'colour': 'blue'}, {'user': 'xavier', 'colour': 'green'}]

```

# Min and Max
Use to find min/max value of an iterable
```
>>> min(3,44,5,3,2)
2
>>> max(3,44,5,3,2)
44
```

Can also run against lists of dicts in a similar way to any/all
```
users = [
  {'user': 'tob', 'colour': 'blue', 'fav_num': 99},
  {'user': 'xavier', 'colour': 'green', 'fav_num': 33},
  {'user': 'cob', 'colour': 'red', 'fav_num': 2}
]

>>> min(users, key=lambda n: n['fav_num'])
{'user': 'cob', 'colour': 'red', 'fav_num': 2}
>>> max(users, key=lambda n: n['fav_num'])
{'user': 'tob', 'colour': 'blue', 'fav_num': 99}
>>> max(users, key=lambda n: n['fav_num'])['user']
'tob'
```

# Reversed (not the same as the list.reverse())
Returns a reverse iterator object.
```
>>> nums
[1, 2, 4, 6, 54, 646]
>>> reversed(nums)
<list_reverseiterator object at 0x102bf4a60>

>>> list(reversed(range(1,10)))
[9, 8, 7, 6, 5, 4, 3, 2, 1]

>>> [x for x in reversed(range(1,10))]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

# abs
Takes a number and returns the absolute value (basically returns a non negative number)

```
>>> abs(4)
4
>>> abs(-4)
4
>>> abs(4.5555)
4.5555
>>> abs(-4.5555)
4.5555
```
Can use math.fabs (import math), to treat as float.

# sum
Takes an iterable and optional start
Returns the sum of start and the items of an iterable from left to right and returns the total.

```
>>> sum([1,2,3])
6
>>> sum([1,2,3], 10)
16
>>> sum([1,2,3], -10)
-4
>>> sum([1,2,3], 20)
26
```

# round
Return number rounded to ndigits precision after the decimal point.
IF ndigits is omitted or is None, it returns the integer nearest to its input
```
>>> round(4.567)
5
>>> round(4.2567)
4
>>> round(4.2567, 1)
4.3
```

# zip
Makes 
