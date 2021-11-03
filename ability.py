import random

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = max_damage
  
  def attack(self):
    damage = random.randint(0, self.max_damage)
    return damage
   
  pass