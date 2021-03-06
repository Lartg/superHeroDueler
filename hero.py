import random
from ability import Ability
from armor import Armor
from weapon import Weapon

heroes = []

class Hero:
  #set parameters of hero
  def __init__(self, name, starting_health=100):
    #hero properties
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0

    #store abilities and defenses of hero
    self.abilities = []
    self.armor = []
    
    #add to list of heroes that can be accessed globally
    heroes.append(self)
  
  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def attack(self):
    damage_output = 0
    for ability in self.abilities:
      damage_output += ability.attack()
    return damage_output

  def add_armor(self, armor):
    self.armor.append(armor)

  def defend(self):
    damage_blocked = 0
    for armor in self.armor:
      damage_blocked += armor.block()
    return damage_blocked

  def fight(self, opponent):
    if(len(self.abilities) == 0 and len(opponent.abilities) == 0):
      return print("draw")
    opponent.alive = True
    self.alive = True
    while self.alive == True and opponent.alive == True:
      opponent.current_health -= self.attack() - opponent.defend()
      self.current_health -= opponent.attack() - self.defend()
      self.alive = self.is_alive()
      opponent.alive = opponent.is_alive()
    if self.alive == False and opponent.alive == False:
      self.add_kill(1)
      opponent.add_death(1)
      self.add_death(1)
      opponent.add_kill(1)
      return print(f"In a duel between {self.name} and {opponent.name}...\nBoth have perished!")
    elif self.alive == True:
      self.add_kill(1)
      opponent.add_death(1)
      return print(f"In a duel between {self.name} and {opponent.name}...\nThe Victor!\nIs!\n{self.name}")
    elif opponent.alive == True:
      self.add_death(1)
      opponent.add_kill(1)
      return print(f"In a duel between {self.name} and {opponent.name}...\nThe Victor!\nIs!\n{opponent.name}")
    else:
      return print("error")
  def fight_random_opponent(self):

    #so that opponent is random, but never themselves
    #we loop until the opponent != self
    opponent = self
    while opponent == self:
      opponent = random.choice(heroes)

    #call fight method
    self.fight(opponent)
  
  def take_damage(self, damage_incoming):
    damage_dealt = damage_incoming - self.defend()
    if damage_dealt > 0:
      self.current_health -= damage_dealt

  def is_alive(self):
    if self.current_health > 0:
      return True
    else:
      return False
  
  def add_kill(self, num_kills):
    self.kills += num_kills

  def add_death(self, num_deaths):
    self.deaths += num_deaths
  
  pass