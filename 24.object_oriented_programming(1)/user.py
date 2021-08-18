# Defining the simplest possible class

# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#     pass
#
# user1 = User("dave", "smith",22)
# user2 = User("jane","doe",44)
# print(user1.first)
# print(user2.first, user2.last, user2.age)

class Person:
    def __init__(self):
        self.name = "tony"
        self._secret = "hi" # Private attribute by convention only - can still call if need to.
        self.__msg = "I like turtles" # name mangling see output below
p = Person()
print(p.name)
print(p._secret)
print(dir(p))
