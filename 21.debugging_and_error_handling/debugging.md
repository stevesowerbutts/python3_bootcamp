# Common error types (built-in exceptions)

SyntaxError
- Incorrect Syntax, pyton cant parse (typos etc)

NameError
- Variable is not defined

TypeError
- Mismatch of datatypes
- eg. adding a string to a list
```
>>> 'hello' + 5
TypeError: can only concatenate str (not "int") to str

>>> len(5)
TypeError: object of type 'int' has no len()
```

IndexError
- Try to access an element in list using invalid index (one that is outside of the the range of the list/string)
```
>>> 'hello'[8]
IndexError: string index out of range
```

ValueError
- Operation of function receives and argument of correct type, but inappropriate value
```
>>> int('foo')
ValueError: invalid literal for int() with base 10: 'foo'
>>> int('10')
10
```

KeyError
- dict does not have a specific key
```
d = {}
>>> d['foo']
KeyError: 'foo'
```
AttributeError
- When a variable does not have an attribute
```
>>> "awesome".foo
AttributeError: 'str' object has no attribute 'foo'
```

# Raise your own exceptions
In python can throw errors using the `raise` keyword
```
>>> raise NameError("blah")
NameError: blah
```

# Try and Except blocks
Strongly encouraged to use try/except blocks
- Should always be specific
```
>>> try:
...     foobar
... except NameError:
...     print("NameError - Problem")
...
NameError - Problem
```

# try, except, else, finally
- `try` - will try to run something
- `except` - will run if try doesnt
- `else` runs when except does not
- `finally` runs last no matter what

See try2.py and divide.py for examples

# debugging with pdb (python debugger)

To set breakpoints in code use pdb by inserting the below line:
```
import pdb; pdb.set_trace()
```
see examples in debugging.py
```$ python3 ./21.debugging_and_error_handling/debugging.py
-> result = first + second
(Pdb) first
'First'
(Pdb) result
*** NameError: name 'result' is not defined
(Pdb) l     ### Lists where you are in the script
  1  	# FIRST EXAMPLE:
  2  	import pdb
  3  	first = "First"
  4  	second = "Second"
  5  	pdb.set_trace()
  6  ->	result = first + second
  7  	third = "Third"
  8  	result += third
  9  	print(result)

(Pdb) n     ### Moves to the next line
-> third = "Third"
(Pdb) result
'FirstSecond'
```
