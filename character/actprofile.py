from character.action import Action
from dice.dice import checkTwenty

class ActionProfile:
#'Collection of Actions'
    prof = []

    def __init__(self):
        return

    def addAction(self, act):
        self.prof.append(act)
        print(self.prof)
        return

    def delAction(self, act):
        tempProf = self.prof
        for i, x in enumerate(self.prof):
            if x.isEqual(act):
                del tempProf[i]
        self.prof = tempProf
        return

    def getRoll(self, n):
        checkTwenty(n)
        ret = []
        for x in self.prof:
            print(x)
            y = x.getRoll(n)
            if y:
                ret.append(x)
        return ret

    def getSpread(self):
        ret = []
        ret.append([])
        for n in xrange(1,20):
            ret.append(self.getRoll(n))
        return ret
