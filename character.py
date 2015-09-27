from entity import Entity
from klass import Klass
from game import Game

class Character(Entity):
    def __init__(self):
        self.set_random_abilities()
        self.welcome()
        self.name = raw_input('Enter your name: ')
        self.klass = self.choose_klass()
        self.hp = 10
        self.base_attack_bonus = 2
        self.damage = 2

    def welcome(self):
        print("Welcome, hero!")
        print(self.abilities)
    def choose_klass(self):
        options = []
        for klass in Klass.ALL_KLASSES:
            options.append(klass.name)
        choice = Game.choose_index_from_options(options)
        klass = Klass.ALL_KLASSES[choice]
        print("Chose {}.".format(klass.name))
        return klass


joe = Character()
