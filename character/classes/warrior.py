from character.character import Character
from character.action import Action
from ability.attack import Attack
from ability.potion import Potion

class Warrior(Character):
    def __init__(self, lvl):
        if lvl == 1:
            Character.__init__(self, 7, 5, 3, 2)
            self.warriorCleave()
            self.warriorPotion()
        else:
            raise Exception("Fail to create Warrior!")
            quit()


    def warriorCleave(self):
        hits = [20]
        if(self.getDx() >= 2):
            hits.append(19)
        if(self.getDx() >= 4):
            hits.append(18)
        if(self.getDx() >= 6):
            hits.append(17)
        cleaveab = Attack(self.getSt()) # maybe add item here
        warriorcleave = Action("Warrior Cleave", cleaveab, hits)
        self.addAction(warriorcleave)
        return

    def warriorPotion(self):
        hits = [5]
        potab = Potion(1)
        pot = Action("Potion", potab, hits)
        self.addAction(pot)
        return
