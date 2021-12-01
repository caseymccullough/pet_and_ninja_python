class Pet:

   # NOTE noise needs to be added as data member
   def __init__(self, name , species , tricks, energy, health, sound ):
      self.name = name
      self.species = species
      self.tricks = tricks
      self.energy = energy
      self.health = health
      self.sound = sound

   # sleep() - increases the pets energy by 25
   def sleep(self):
      self.energy += 25
      print (f"{self.name} is energized by their nap")
      return self

   # eat() - increases the pet's energy by 5 & health by 10
   def eat(self):
       self.energy += 5
       self.health += 10
       print (f"{self.name} gobbles up their food")
       return self

   # play() - increases the pet's health by 5
   def play(self):
      self.health += 5
      print (f"{self.name}--It's playtime!!")
      return self

   # noise() - prints out the pet's sound
   def noise (self):
      print(3 * (self.sound + " "))
      return self

