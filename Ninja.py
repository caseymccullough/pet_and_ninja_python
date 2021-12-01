class Ninja:
   def __init__(self, first_name , last_name , treats , pet_food , pet ):
      self.first_name = first_name
      self.last_name = last_name
      self.treats = treats
      self.pet_food = pet_food
      self.pet = pet
        	
   # - walks the ninja's pet invoking the pet play() method
   def walk(self):
      print("taking the pet for a walk")
      self.pet.play()
      return self
   
   # feed() - feeds the ninja's pet invoking the pet eat() method
   def feed(self):
      print("feeding the pet")
      self.pet.eat()
      self.pet_food -= 5
      return self

   # bathe() - cleans the ninja's pet invoking the pet noise() method
   def bathe(self):
      print("bathing the pet")
      self.pet.noise()
      return self

