from ability.ability import Ability
from effect.hit import Hit

class Attack(Ability):
    def __init__(self, power):
        h = Hit(power)
        self.fx = h
        self.verb = "attack"
        return
