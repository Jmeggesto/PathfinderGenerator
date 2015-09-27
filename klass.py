class Klass:
    GOOD_BAB_PROGRESSION = 1
    MEDIUM_BAB_PROGRESSION = 2
    POOR_BAB_PROGRESSION = 3

    GOOD_SAVE_PROGRESSION = 1
    POOR_SAVE_PROGRESSION = 2

class Fighter:
    name = "Fighter"
    hit_die = 10
    starting_wealth = 175
    base_attack_bonus = Klass.GOOD_BAB_PROGRESSION
    fortitude = Klass.GOOD_SAVE_PROGRESSION
    reflex = Klass.POOR_SAVE_PROGRESSION
    will = Klass.POOR_SAVE_PROGRESSION
    proficiency = {
        "weapon" : [
            "simple",
            "martial"
        ],
        "armor" : [
            "heavy",
            "light",
            "medium",
            "shields"
        ]
        #treat armor as level-based? i.e., lvl 0 = no proficiency, lvl 2 is medium and light
    }
    #class_skills?
    #feats?

class Cleric:
    name = "Cleric"
    hit_die = 8
    starting_wealth = 140
    base_attack_bonus = Klass.MEDIUM_BAB_PROGRESSION
    fortitude = Klass.GOOD_SAVE_PROGRESSION
    reflex = Klass.POOR_SAVE_PROGRESSION
    will = Klass.GOOD_SAVE_PROGRESSION
    proficiency = {
        "weapon" : [
            "simple",
            "martial"
        ],
        "armor" : [
            "medium",
            "light",
            "shields"
        ]
    }
    #spells

Klass.ALL_KLASSES = [Fighter, Cleric]
