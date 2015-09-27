from entity import Entity
from klass import Klass
from game import Game

class Character(Entity):
    def __init__(self):
        self.set_random_abilities()
        self.welcome()
        self.name = raw_input('Enter your name: ')
        self.klass = self.choose_klass()
        self.max_hp = self.set_max_hp()
        self.base_attack_bonus = self.set_bab()
        self.damage = 2

    def welcome(self):
        print("Welcome, hero!")
        print(self.abilities)

    def choose_klass(self):
        options = []
        for klass in Klass.ALL_KLASSES:
            options.append(klass.name)
        choice = Game.choose_index_from_options(options)
        return Klass.ALL_KLASSES[choice]

    def set_max_hp(self):
        return self.ability_mods["Con"] + self.klass.hit_die

    def set_bab(self):
        bab_type = self.klass.base_attack_bonus
        if bab_type == Klass.GOOD_BAB_PROGRESSION:
            return self.good_bab_progression()
        elif bab_type == Klass.MEDIUM_BAB_PROGRESSION:
            return self.medium_bab_progression()
        else:
            return self.poor_bab_progression()


joe = Character()
print(joe.base_attack_bonus)
