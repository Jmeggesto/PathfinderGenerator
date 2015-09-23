import random

def fourd6_drop_lowest():
    rolls = [random.randint(1, 6) for i in range(4)]
    return sum(sorted(rolls)[1:])

def random_abilities(base = None):
    if base is None:
        base = {ability : 0 for ability in ["Str", "Dex", "Con", "Int", "Wis", "Cha"]}

    for ability in base:
        base[ability] += fourd6_drop_lowest()

    return base

class Entity():

    def __init__(self,
                name = '',
                hp = 0, 
                base_attack_bonus = 0,
                damage = 0
            ):
        self.name = name
        self.hp = hp
        self.abilities = random_abilities()
        self.ability_mods = {ability : score // 2 - 5 for ability, score in self.abilities.items()}
        self.base_attack_bonus = base_attack_bonus
        self.damage = damage
    	
    	

