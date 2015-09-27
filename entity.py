import random
import math
import klass

class Entity(object):
    lvl = 1
    def __init__(self, **kwargs):

        self.name = kwargs.get('name')
        self.set_random_abilities()
        self.klass = kwargs.get('class')
        self.max_hp = 10
        self.hp = 10
        self.base_attack_bonus = 0

    # generate random ability scores
    def fourd6_drop_lowest(self):
        rolls = [random.randint(1, 6) for i in range(4)]
        return sum(sorted(rolls)[1:])
    def set_random_abilities(self, base = None):
        if base is None:
            base = {ability : 0 for ability in ["Str", "Dex", "Con", "Int", "Wis", "Cha"]}
        for ability in base:
            base[ability] += self.fourd6_drop_lowest()
        self.abilities = base
        self.updateMods()
    def updateMods(self):
        self.ability_mods = {ability : score // 2 - 5 for ability, score in self.abilities.items()}

    # generic lvl up progression
    def good_bab_progression(self):
        return int(math.floor(self.lvl))
    def medium_bab_progression(self):
        return int(math.floor(self.lvl*3/4))
    def poor_bab_progression(self):
        return int(math.floor(self.lvl/2))

    def good_save_progression(self):
        return int(math.floor(2 + self.lvl/2))
    def poor_save_progression(self):
        return int(math.floor(self.lvl/3))
