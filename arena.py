from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self, name1, name2):
    self.team_one = Team(name1)
    self.team_two = Team(name2)
  
  def create_ability(self):
    name = input("Ability name:  ")
    max_damage = int(input("Max damage:  "))
    return Ability(name, max_damage)
  
  def create_armor(self):
    name = input("Armor name:  ")
    max_block = int(input("Max block:  "))
    return Armor(name, max_block)
  
  def create_hero(self):
    name = input("Hero name:  ")
    health = int(input("Hero health (enter a number):  "))
    
    hero = Hero(name, health)

    add_item = None
    while add_item != 4:
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        hero.abilities.append(self.create_ability())
      elif add_item == "2":
        hero.abilities.append(Weapon(self.create_ability()))
      elif add_item == "3":
        hero.armor.append(self.create_armor())
      elif add_item == "4":
        add_item = 4
    return hero
  
  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  def build_team_two(self):
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_two.add_hero(hero)

  def team_battle(self):
    self.team_one.attack(self.team_two)
    
  def show_stats(self):
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")
  
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    team_kills = 0
    team_deaths = 0
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))
  
  pass