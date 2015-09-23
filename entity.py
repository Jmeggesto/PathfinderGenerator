import random


def fourd6_drop_lowest():
    rolls = []
    [rolls.append(random.randint(1, 6)) for i in range(1, 5)]
    return sum([roll for roll in rolls if roll is not min(rolls)])

def random_abilities(base = None):
    if base is None:
        base = {ability : 0 for ability in ["Str", "Dex", "Con", "Int", "Wis", "Cha"]}

    for ability in base:
        base[ability] = fourd6_drop_lowest()
    return base

class Entity():
	def __init__(self,
				 name = '',
				 hp = 0,
				 abilities = {},
				 ability_mods = {},
				 base_attack_bonus = 0,
				 damage = 0
				 ):
		self.name = name
		self.hp = hp
		self.abilities = random_abilities()
		self.ability_mods = {ability : int(self.abilities[ability] / 2 - 5) for ability in self.abilities}
		self.base_attack_bonus = base_attack_bonus
		self.damage = damage

