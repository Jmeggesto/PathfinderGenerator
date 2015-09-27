import random
class Entity(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.set_random_abilities()
        self.klass = kwargs.get('class')
        self.hp = 10
        self.base_attack_bonus = 2
        self.damage = 2

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
