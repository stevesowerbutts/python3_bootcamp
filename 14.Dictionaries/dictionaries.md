# Dictionaries

key value pairs wrapped in `{}`

eg. `cat = {'name':'blue', 'age': 2}`

Can also use the `dict` function:
eg.
```
cat2 = dict(name = 'kitty', age=3)`
cat2 == {'name':'kitty', 'age':3}
```

If you know the key you need to extract:
```
artist = {
   "first": "Neil",
   "last": "Young",
}

artist['first'] == 'Neil'

>>> fulname = f"{artist['first']} {artist['last']}"
>>> fulname
'Neil Young'
```

Dict functions:
`.keys()` - returns only the keys
`.values()` - returns only the values
`.items()` - returns all keys and values

```
>>> artist.keys()
dict_keys(['first', 'last'])
>>> artist.values()
dict_values(['Neil', 'Young'])
>>> artist.items()
dict_items([('first', 'Neil'), ('last', 'Young')])
```

# Iterating over Dictionaries

Can loop through dict using the dict functions:
```
>>> for key, value in artist.items():
...     print(key,value)
...
first Neil
last Young
```


1. Loop over donations to add all values
```
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
>>> for i in donations.values():
...     total_donations += i
>>> total_donations
436.74

total_donations = sum(donations.values())
>>> total_donations
436.74
```

# Check if key or value in dict

By default the keyword `in` checks the dict keys:
```
artist = {
   "first": "Neil",
   "last": "Young",
}

'first' in artist # True`
'full_name' in artist # False
'Neil' in artist # False
```

To check in values need to use .values:
```
"Neil" in artist.values() # True
"first" in artist.values() # False
```

# Dict methods
You can get values out of a list using `[]` - **Will throw key error if it doesnt exist**
eg.
```
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
inventory['bagel']
4
```
clear() - empties a dict
copy() - copies dict (looks the same but stored separately in memory)
```
>>> inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
>>> stock_list = {}.copy(inventory)
```
fromkeys() - Creates key-value pairs from comma separated values
  - Usually used to create default/template dict before we know values
  - eg. New user:
  ```
  new_user = {}.fromkeys(['name', 'age', 'bio'], 'unknown')
  >>> new_user
  {'name': 'unknown', 'age': 'unknown', 'bio': 'unknown'}
  ```
  ```
  game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
  initial_game_state = {}.fromkeys(game_properties, 0)
  >>> initial_game_state
  {'current_score': 0, 'high_score': 0, 'number_of_lives': 0, 'items_in_inventory': 0, 'power_ups': 0, 'ammo': 0, 'enemies_on_screen': 0, 'enemy_kills': 0, 'enemy_kill_streaks': 0, 'minutes_played': 0, 'notifications': 0, 'achievements': 0}
  ```

get() - retrieves key in an object and returns a value, **returns `None` if the key doesnt exist rather than throwing an error.**
```
>>> donations = {'sam': 25.0, 'lena': 88.99, 'chuck': 13.0, 'linus': 99.5, 'stan': 150.0, 'lisa': 50.25, 'harrison': 10.0}
>>> donations.get('sam')
25.0
>>> donations.get('tom')
>>>
```


pop() - pops the `value` from the dict
popitem() - default removes random item from dict

update() - update keys and values from a dict (doesnt remove things but will overwrite)

# Dict  ehensions
Iterates over keys by default
Iterate over keys and values using .items()

Syntax: `{__:__ for __ in __}`
eg.
```
>>> numbers = dict(first=1,second=2,third=3)
>>> {key: value ** 2 for key,value in numbers.items()}
{'first': 1, 'second': 4, 'third': 9}
```

Can also use to create a dict from a list
```
>>> {num: num**2 for num in [1,2,3,4,5]}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Conditional logic

```
>>> num_list =  [1,2,3,4,5]
>>> {num:("even" if num % 2 == 0 else "odd") for num in num_list}
{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

>>> {num:("even" if num % 2 == 0 else "odd") for num in range(0,21)}
{0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even', 11: 'odd', 12: 'even', 13: 'odd', 14: 'even', 15: 'odd', 16: 'even', 17: 'odd', 18: 'even', 19: 'odd', 20: 'even'}
```

Merging lists into dicts
  - Need to loop through the values in each list using range/len so that values can be indexed.
  - Simpler (Advanced) version of this can be achieved using `zip()`

```
>>> list1 = ['CA', 'NJ', 'RI']
>>> list2 = ['California', 'New Jersey', 'Rhode Island']

>>> {list1[i]:list2[i] for i in range(0,len(list1))}
{'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

>>> dict(zip(list1,list2))
{'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
```

If you have a list of pairs, you can convert to a dictionary using `dict()`
```
>>> person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

>>> {k:v for k,v in person}
{'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

>>> dict(person)
{'name': 'Jared', 'job': 'Musician', 'city': 'Bern'
```
