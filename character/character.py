from character.actprofile import ActionProfile
from effect.effect import Effect
#from item.weapon import Weapon
#from item.armor import Armor
#from item.relic import Relic

class Character:
    hp = 1 # hitpoints
    st = 1 # strength
    dx = 1 # dexterity
    ws = 1 # wisdom
    act = ActionProfile()
    wp = None #weapon
    ar = None #armor
    rl = None #relic
    fx = []

    def __init__(self, h, s, d, w):
        self.hp = h
        self.st = s
        self.dx = d
        self.ws = w
        return;

    def setWeapon(self, w):
        self.wp = w
        return
    def getWeapon(self):
        return self.wp
    def setArmor(self, a):
        self.ar = a
        return
    def getArmor(self):
        return self.ar
    def setRelic(self, r):
        self.rl = r
        return
    def getRelic(self):
        return self.rl
    def getHp(self):
        return self.hp
    def isAlive(self):
        return (self.hp > 0)
    def getSt(self):
        return self.st
    def getDx(self):
        return self.dx
    def getWs(self):
        return self.ws

    def setHit(self, h):
        #take damage and return whether character is still alive
        self.hp = self.hp - h
        return self.isAlive()

    def addFx(self, e):
        self.fx.append(e)

    def addHit(self, h):
        hp = hp + h
        return

    def addAction(self, at):
        print("addaction")
        print(at)
        self.act.addAction(at)
        return

    def goRoll(self, n):
        ret = []
        p = self.act.getRoll(n)
        print(p)
        for x in p:
            ret.append(p.getAbl())
        return ret

    def takeEffect(self):
        for e in self.fx:
            if e.name == "hit":
                self.setHit(e.getPow)
            elif e.name == "heal":
                self.hp = self.hp + e.getPow
            else:
                raise Exception("Unknown effect on character!")
                quit()
        self.cleanEffect()
        return

    def cleanEffect(self):
        self.fx = [e for e in self.fx if e.tick()]
