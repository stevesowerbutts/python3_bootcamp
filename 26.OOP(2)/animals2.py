class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"



class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"



class Penguin(Ambulatory, Aquatic):
  def __init__(self,name):
    print("PENGUIN INIT!")
    super().__init__(name=name)
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")















# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??
























