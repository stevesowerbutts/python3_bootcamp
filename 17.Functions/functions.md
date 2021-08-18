# Functions

Process for executing a task - reusable

DRY - Dont Repeat Yourself

def name_of_function():
  # block of runnable code

```
def sing_happy_birthday():
    print("Happy birthday to you")
```


## Return
return a value from a function.
Exits the function - nothing runs after the return statement

Outputs whatever value is placed after the return keyword - can use a tuple for multiple values
pops the function off the call stack

## Common return mistakes
1. Check indentation
2. Unnecessary else
```
def is_odd_number(num):
  if num % 2 != 0:
      return True
  else:
      return False

# Dont need the else statement
def is_odd_number(num):
  if num % 2 != 0:
      return True
  return False

>>> is_odd_number(4)
False
```


## Inputs

Parameters should have names that make sense:
```
def print_name(first_name, Last_name):
    print(f"Hello {first_name} {Last_name}")

print_name("ste", "james")
Hello ste james
```


## Default Parameters

Add defaut Parameters by passing value after `=`:
```
>>> def exponent(num, power=2):
...     return num ** power
...
>>> exponent(2,3)
8
>>> exponent(2)
4
```
Allows you to be more defensive
avoids errors with incorrect Parameters
more readable examples

Default functions can be anything - string, list, dict, bool or even other functions.

Params are read/passed in order, so params with defaults should be at the end, or all params should have defaults.  
```
>>> def add(a,b):
...     return a+b
...
>>> def math(fn=add, a,b):
...     return fn(a,b)
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

```
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

# Better way to write the above using dict

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

```

## Keyword arguments
keyword arguments allow you to change the order of params
bit more flexible

When you define a function and use an `=` you are setting a default Parameter
when you call a function and use an `=` you are making a keyword argument

## Scope

Variables created in a function are scoped in that function (only available in the function)
eg.
```
instructor = "Mary" # available anywhere
def print_name():
    return f'Hello {instructor}'

def print_name():
    instructor = 'colt' # Only available inside this function
    return f'Hello {instructor}'

>>> print_name()
'Hello colt'
>>> print(instructor)
Mary
```

## Global

Variables not defined inside functions - try to minimise use
Have to specify global function if you want to manipulate that variable inside a function - by default functions try to use local variables
```
total = 0

def increment():
    total += 1
    return total
>>> increment()
UnboundLocalError: local variable 'total' referenced before assignment

def increment():
    global total # Have to specify the global variable
    total += 1
    return total
>>> increment()
1
```

## nonlocal
Lets us modify parents variables in a child(nested) function
```
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
```


## Documenting functions
Docstrings used to document what functions do
can get a functions docstring using `function.__doc__`
```
def say_hello():
    """A Simple Function that returns the string hello"""
    return "Hello!"

>>> say_hello.__doc__
'A Simple Function that returns the string hello'
```
