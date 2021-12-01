from Ninja import Ninja
from Pet import Pet

# (self, name , species , tricks, energy, health, sound ):
luna = Pet("Luna", "Dog", [], 100, 200, "bark")

luna.noise()

# (self, first_name , last_name , treats , pet_food , pet ):
casey = Ninja("Casey", "McCullough", 25, 40, luna)

casey.walk().feed().bathe()


