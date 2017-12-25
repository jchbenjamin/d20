from character.character import Character
from character.action import Action
from ability.attack import Attack

class Goblin(Character):
    def __init__(self, lvl):
        if lvl == 1:
            Character.__init__(self, 5, 2, 2, 1)
            self.goblinSwipe()
        else:
            raise Exception("Fail to create Goblin!")
            quit()

    def goblinSwipe(self):
        hits = [20]
        if(self.getDx() >= 2):
            hits.append(19)
        if(self.getDx() >= 4):
            hits.append(18)
        swipeab = Attack(self.getSt())
        goblinswipe = Action("Goblin Swipe", swipeab, hits)
        self.addAction(goblinswipe)
        return
