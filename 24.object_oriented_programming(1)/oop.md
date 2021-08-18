# Object oriented Programming
Most languages are object oriented
OOP is a method of programming that attempts to model some process or thing in the world as a *class* or *object*

### Clases & Objects
class - blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)

instance - objects that are constructed from a class blueprint that contain their class' methods and properties

### Why OOP?
The goal is to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about
your code at a higher level.

### Private vs public
Private attributes do not need to be accessed outside of the class/function, vs public methods that are called:

In python there is no true `private` attributes, no way to stop it from being access from outside, however for
differentiations they are names with an underscore in front `_thing` like below:

_cards - (private attribute)
shuffle - (public method)

* Encapsulation
  - The grouping of public and private attributes and methods into a programmatic class, making abstraction possible.
* Abstraction
  - exposing only relevant data in a class interface, hiding private attributes and methods (ie. inner workings) from users.

### Creating a class
Classes in python can have a special __init__ method, which gets called evry time you create an instancce of the class (instantiate)

self keyword refers to the specific, current instance of the class
```
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    pass

user1 = User("dave", "smith",22)
user2 = User("jane","doe",44)
print(user1.first)
```

### Name mangling
Double underscore before the object `__msg`
Sole purpose is to make the method/attribute particular to that class.
Puts the class Name in the attribute.

Another class might inherit from this class, use name manlging to stop any conflicts during inheritance.
```
class Person:
  def __init__(self):
    self.name = "tony"
    self._secret = "hi" # Private attribute by convention only - can still call if need to.
    self.__msg = "I like turtles" # name mangling see output below

p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)

>>>
tony
hi
['_Person__msg', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_secret', 'name']
I like turtles
```

### Instance methods
Every instance of the class has the instance method (see user_methods.py)
```
class User:
	def __init__(self, first, last, age):
		self.first = first # instance attribute
		self.last = last
		self.age = age

	def full_name(self): # instance method
		return f"{self.first} {self.last}"

	def likes(self, thing): # instance method
		return f"{self.first} likes {thing}"
```


### Class attributes
Assign attributes directly on a class that are shared by all instances of a class and the class itself
```
class User:

  active_users = 0

	def __init__(self, first, last, age):
		self.first = first # instance attribute
		self.last = last
		self.age = age
    User.active_users += 1

print(User.active_users) # returns 0
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users) # returns 2
```

### Class methods

Class methods are methods (with the @classmethod decorator) that are not concerned with the instances but the class itself.
ie. if you need to do something with the data before its passed to the instances:
  eg. Convert a string into variables before passing variables to instances.

```
class User:

	active_users = 0

  @classmethod
  def display_active_users(cls):
    print(cls)

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"
```

### String representation

The `__repr__` method is one of several ways to provide a nicer string representation.
  - You get the same thing when you print, or use str to convert to a string.
```
class Human:
    def __init__(self, name="somebody"):
        self.name = name
    def __repr__(self):
        return self.name
>>> due = Human()
>>> print(due)
somebody
```
