import random
from ability import Ability
from armor import Armor


heroes = []

class Hero:
  #set parameters of hero
  def __init__(self, name, starting_health=100):
    #hero properties
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    #store abilities and defenses of hero
    self.abilities = []
    self.armor = []
    
    #add to list of heroes that can be accessed globally
    heroes.append(self)
  
  def add_ability(self, ability):
    self.abilities.append(ability)

  def fight(self, opponent):
    #store fighters in a list then make a weighted choice based upon available stats
    fighters = [opponent, self]
    
    #because random choices must return a list of string, we use an index to select the winner
    index = [0,1]
    winner = random.choices(index, weights=(opponent.current_health, self.current_health), k=1)
    
    #display results
    print(f"In a duel between {fighters[0].name} and {fighters[1].name}...\nThe Victor!\nIs!\n{fighters[winner[0]].name}")
  def fight_random_opponent(self):
    #so that opponent is random, but never themselves
    #we loop until the opponent != self
    opponent = self
    while opponent == self:
      opponent = random.choice(heroes)

    #call fight method
    self.fight(opponent)

#initialized  heroes    
hero_1 = Hero("Flash")
hero_2 = Hero("Iron Man")
hero_3 = Hero("Spider-man")
hero_4 = Hero("Goku")
hero_5 = Hero("Green Lanturn")

hero_1.fight(hero_2)
hero_1.fight_random_opponent()