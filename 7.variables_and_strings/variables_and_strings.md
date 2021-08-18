# Variables and Data types

## Variables

### Naming restrictions
1. Must start with a letter or underscore: _cats NOT 2cats
2. Rest of the name must consist of letters, numbers or underscores (no other symbols): cats2 NOT hey@you
3. Names are case sensitive

### Conventions
1. snake_case
2. lowercase with some exceptions:
  * CAPITAL_SNAKE_CASE - Usually refers to constants (eg. PI = 3.14)
  * UpperCamelCase - Usually refers to a class
3. Variables that start with 2 underscores (called "dunder" for double underscore) are supposed to be private or left alone:
  * `__no_touchy__`

### String escape sequences
All start with backslash
eg.
  newline = `\n`
  escaped_quotes = "he said \"hello\""


### User input
Receive input from terminal - `input()`
eg. `kms = input()`

round function: `round(thing_to_round, how_many_decimals)`
  eg. see mileage.py
