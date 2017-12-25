from character.character import Character
from character.action import Action
from ability.attack import Attack
from ability.potion import Potion

class Rogue(Character):
    def __init__(self, lvl):
        if lvl == 1:
            Character.__init__(self, 7, 3, 6, 3)
            self.rogueStab()
            self.roguePotion()
        else:
            raise Exception("Fail to create Warrior!")
            quit()

    def rogueStab(self):
        hits = [20,19]
        if(self.getDx() >= 1):
            hits.append(18)
        if(self.getDx() >= 3):
            hits.append(17)
        if(self.getDx() >= 5):
            hits.append(16)
        stabab = Attack(self.getSt()) # maybe add item here
        roguestab = Action("Rogue Stab", stabab, hits)
        self.addAction(roguestab)
        return

    def roguePotion():
        hits = [2,3]
        potab = Potion(1)
        pot = Action("Potion", potab, hits)
        self.addAction(pot)
        return
