from ability.ability import Ability
from effect.heal import Heal

class Potion(Ability):
    def __init__(self, power):
        h = Heal(power)
        self.effect = h
        self.verb = "quaff"
        return
