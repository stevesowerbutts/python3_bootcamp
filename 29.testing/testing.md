## Testing

## Why you should Test
Reduce bugs in existing code
Ensure that bugs stay fixed

### Test Driven Development
Development begins by writing tests,
once tests are written, write code to make tests pass
Once tests pass, a feature is considered complete

### Red, green, refactor

1. Red - write a test that fails
2. Green - Write the minimal amount of code to make the test pass
3. Refactor - Clean up the code, while ensure the test still passes

## Assertions
We can make simple assertions with the `assert` keyword
assert accepts an expression
Returns None if the expression is truthy
Raises an AssertionError if the expression is truthy
Accepts an optional error message as a 2nd argument

`assert` is a statement, not a function

see assertions.py for examples
```
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1)) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!
```
**Assertions warning**
- if a python file is run with the `-O` flag, assertions will not be evaluated
  - ie. assertion is ignored and the code will try and run.

## doctests
Can write tests for functions inside the docstring, looks like and has to be written like the python repl output
- requires a very specific syntax - see doctest_demo.py
  - Will fail for any syntax differences, like additional white space, order of keys etc.
- requires single quotes
- Can be good for writing tests with documentation

```
def add(a, b):
	"""
	>>> add(2, 3)
	5
	>>> add(100,200)
	300
	"""
	return a + b
```
Run the tests by running the below command:
`python3 -m doctest -v your_file_name.py`

## Intro to unittest

Test small parts of an application in isolation (eg. units)
Good candidats for unit testing:
  - Individual classes, modules or functions
Bad cadidates for unit testing:
  - An entire application, dependencies across several classes/modules

Builtin module called `unittest`
Testing framework, has built in assertions that you inherit from `unittest.TestCase`
Run tests by calling `unittest.main()`

Requires a separate file for the tests (see tests.py)
  - then import what you want to test from the python script (see activities.py)
  - Need to call __main__ at the end to run the tests
```
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I'm eating broccoli, because my body is a temple"
    	)

if __name__ == '__main__':
    unittest.main()
```

### Types of assertions

- self.assertEqual(x, y)
- self.assertNotEqual(x, y)
- self.assertTrue(x)
- self.assertFalse(x)
- self.assertIsNone(x)
- self.assertIsNotNone(x)
- self.assertIn(x, y)
- self.assertNotIn(x, y)

Can also test for errors raised
- self.assertRaises()
- needs a colon after the assert
  ```
  def test_eat_healthy_boolean(self):
      """is_healthy must be a bool"""
      with self.assertRaises(ValueError):
        eat("pizza", is_healthy="who cares?")
  ```


### Before and after hooks

For larger applcations, you may want similar application before running tests
`setUp` runs before each test method
`tearDown` runs after each test method
Common use cases:
- adding/removing data from a test db
- creating instances of a class
