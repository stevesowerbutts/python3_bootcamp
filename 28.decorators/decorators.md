### Higher order Functions
You can pass funcs as args to other functions
  - see higher_order.py

Can nest functions inside one another
  - see nested_function.py
Can also return functions from other functions
  - Inner functions can access outer functions scope
  - see return_func.py


### Intro to decorators

Function that wraps other functions,
enhancing or changing behaviour of the functions being wrapped.
decorators are examples of higher order Functions
Have their own syntax using the `@` (syntactic sugar)

  - dec.py is an example of wrapping functions without using decorator syntax

  - decorate_syntax.py shows how you could write with decorator syntax `@`
  ```
  def be_polite(fn):
      def wrapper():
          print("What a pleasure to meet you!")
          fn()
          print("Have a great day!")
      return wrapper

  @be_polite
  def greet():
      print("My name is Colt.")

  greet()
  # we dont need to set
  # greet = be_polite(greet)
  ```

### Functions with different signatures
- decorator_args.py

The above function would fail if more than 1 arg is passed to the be_polite function (only accepts 1 arg)
  - solution is to use `*args, **kwargs`, so wrapper functions usually accept unlimited args/kwargs
  ```
  def shout(fn):
      def wrapper(*args, **kwargs):
          return fn(*args, **kwargs).upper()
      return wrapper
  ```

### Preserving metadata

Can import wraps from functools
ensures the metadata for the function being wrapped is preserved.
- see metadata.py
