import random


class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = []
  
  def add_hero(self, hero):
    self.heroes.append(hero)
  
  def remove_hero(self, hero):
    found_hero = False
    for hero_member in self.heroes:
      if hero == hero_member:
        self.heroes.remove(hero)
        found_hero = True
    if not found_hero:
      return 0
  
  def view_all_heroes(self):
    print(f"The members of {self.name} are:")
    for hero in self.heroes:
      print(hero.name)
  
  def stats(self):
    for hero in self.heroes:
      deaths = hero.deaths
      if deaths == 0:
        deaths = 1
      kd = hero.kills / deaths
      print(f"{hero.name} KD:{kd}")
  
  def revive_heroes(self):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    living_heroes = []
    living_opponents = []

    for hero in self.heroes:
      living_heroes.append(hero)
    
    for hero in other_team.heroes:
      living_opponents.append(hero)
    
    while len(living_heroes) > 0 and len(living_opponents) > 0:
      hero = random.choice(living_heroes)
      opponent = random.choice(living_opponents)

      hero.fight(opponent)

      if hero.is_alive() == False:
        living_heroes.remove(hero)
      if opponent.is_alive() == False:
        living_opponents.remove(opponent)
  
  pass