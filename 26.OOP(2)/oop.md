# Object orientated programming (part 2)

### Inheritance

Define a class that inherits from another class (a "base" or "parent" class)
Works by passing the parent class as an argument to the definition of a child class.

```
class Animal:
	cool = True
	def make_sound(self, sound):
		print(f"this animal says {sound}")

# Cat class inherits from Animal
class Cat(Animal):
	pass
```

## Intro to super()  
Point of inheritance is to try and avoid duplication.
Can use super() to call __init__ from the parent class
In the example below, the Cat class uses super to get name and species from the Animal parent class

```
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy
```

### Multiple Inheritances
Python allows classes to inherit from more than one parent class
You can use super() to inherit from both parent classes, however better to be more explicit when inheriting from
multiple classes, especially if parent classes have the same method names.

```
class Aquatic:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return "I swim"


class Ambulatory:
    def __init__(self, name):
        self.name = name
    def walk(self):
        return "I walk"


class Penguin(Aquatic,Ambulatory):
    def __init__(self, name):
        super().__init__(name) # Call init on both parent classes

>>> captain_cook = Penguin("captain cook")
>>> print(captain_cook.swim())
I swim
>>> print(captain_cook.walk())
I walk
```

### Method resolution order
When you create a class, python creates a Method Resoltion Order (MRO),
whcih is the Order that python looks for methods on instances of that class.

You can programmatically reference the MRO in three ways:
- __MRO__ attribute on the class
- use mro() method on the clas
- use builtin help(cls) method

```
>>> Penguin.__mro__
(<class '__main__.Penguin'>, <class '__main__.Aquatic'>, <class '__main__.Ambulatory'>, <class 'object'>)

>>> Penguin.mro()
[<class '__main__.Penguin'>, <class '__main__.Aquatic'>, <class '__main__.Ambulatory'>, <class 'object'>]

>>> help(Penguin) # Best for human readability, gives full readme with detailed chain
Help on class Penguin in module __main__:

class Penguin(Aquatic, Ambulatory)
 |  Penguin(name)
 | ......
```


### Polymorphism

Key principle in OOP - an object can take on many forms
Two Practical applications:
1. Same class method works in similar way for different classes
  - Common implementation of this is to have a method in a base(parent) class, that is overridden by a subclass.
    - This is call method overriding (see animals2.py)
  - Each subclass will have a different implementation of the method
2. The same operation works for different kinds of objects - **Special Methods**
  - Python classes have special methods (magic methods) that are dunders (__thing__)
  - These methods with special names that give instructions to python for how to deal with objects

### Special methods
https://docs.python.org/3/reference/datamodel.html#special-method-names

You can use special methods within a class to add additional builtin functionality:
eg. the + operator is shorthand for the __add__() special method
If the two objects are integers it will do mathmatical addition, if strings it will concat them.
  - You can declare special methods in your classes to mimic the behaviour of builtin objects, like __add__ or __len__ etc.

   
