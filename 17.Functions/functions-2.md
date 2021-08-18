# Functions part 2

## *args
Special operator that we can pass to Functions
Gathers remaining arguments as a *tuple*
This is a parameter, can call it whatever you want.

Can pass any number of args to a function - saves having to reference every single parameter
eg.
```
def sum_all_vars(*args):
    total = 0
    for val in args:
        total += val
    return total

>>> sum_all_vars(1,2,3,4,5)
15

>>> sum_all_vars(1,2,3,4,5,6,7,8,9,10)
55
```
Can be any type of args:
eg.
```
def contains_purple(*args):
    '''
    >>> contains_purple(25,2,4,'hello')
    False
    >>> contains_purple(25,2,4,'hello','purple')
    True
    '''
    if "purple" in args:
        return True
    return False

>>> contains_purple(25,2,4,'hello')
False
>>> contains_purple(25,2,4,'hello','purple')
True
```

## **kwargs
Another special operator passed to functions`
Gathers remaining keyword arguments as a dict
Can also name the param however you want.

eg. Use kwargs to combine words:
```
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

>>> combine_words('hello',prefix='world')
'worldhello'
>>> combine_words('hello',suffix='world')
'helloworld'
>>> combine_words('hello')
'hello'
```

# Parameter ordering

1. Parameters
2. *args - (returns tuple - collects all args before default/kwargs) - Single item tuple looks like => `(3,)`
3. default parameters
4. **kwargs - (returns dictionary of kwargs)

You dont need to use all four, however whichever you use still need to be in this order.
eg.

```
def display_info(a, b, *args, instructor="colt", **kwargs):
    return [a, b, args, instructor, kwargs]

>>> display_info(1,2,3, last_name="Steele", job="Instructor")
[1, 2, (3,), 'colt', {'last_name': 'Steele', 'job': 'Instructor'}]
```

## Argument Unpacking
We can use * as an argument to a function to *unpack values*
By default if you pass a list (or tuple) to *args it would be saved as a single object in a tuple.
You can unpack the list by passing the argument with a `*` in front
eg.

```
def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

>>> sum_all_values(1,2,3,4,5) # Individual arguments passed to the function
(1, 2, 3, 4, 5)
15
>>> nums = [1,2,3,4,5]
>>> sum_all_values(nums) # List passed to function as a single tuple item
([1, 2, 3, 4, 5],)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in sum_all_values
TypeError: unsupported operand type(s) for +=: 'int' and 'list'

>>> sum_all_values(*nums) # Tuple/list has been unpacked to Individual arguments
(1, 2, 3, 4, 5)
15
```

## dictionary unpacking
Can use `**` to unpack dictionary arg
```
def display_names(first, second):
    print(f'{first} says hello to {second}')

>>> display_names(first="Charlie", second="Sue")
Charlie says hello to Sue

>>> names = {'first':'Steve', 'second':'James'}

>>> display_names(names)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: display_names() missing 1 required positional argument: 'second'

>>> display_names(**names)
Steve says hello to James
```
