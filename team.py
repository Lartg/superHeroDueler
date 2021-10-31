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
        self.heroes.remove(hero_member)
        found_hero = True
    if not found_hero:
      return 0
  
  def display_team_members(self):
    print(f"The members of {self.name} are:")
    for hero in self.heroes:
      print(hero.name)
  