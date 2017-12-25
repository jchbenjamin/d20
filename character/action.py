from dice.dice import checkTwenty
from ability.ability import Ability

class Action:
#    'Define actions a Character can take'
    name = ""
    abl = None
    rollValues = []

    def __init__(self, n, a, i):
        self.name = n
        self.abl = a
        self.setRoll(i)
        return

    def getName(self):
        return self.name

    def isEqual(self, act):
        if self.name == act.getName:
            return true
        else:
            return false

    def setRoll(self, i):
        for x in i:
            checkTwenty(x)
            self.rollValues.append(x)
        return

    def getAbl(self):
        return self.abl

    def getRoll(self, n):
        checkTwenty(n)
        ret = []
        for x in self.rollValues:
            if x == n:
                return True
        return False
