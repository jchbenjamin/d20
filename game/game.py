from dice.dice import Dice
from character.character import Character
from character.classes.goblin import Goblin
from character.classes.warrior import Warrior
from character.classes.rogue import Rogue

class Game:
    'define the game state'
    state = 0
    playerOne = None #Warrior(1)
    playerTwo = None #Goblin(1)
    d = Dice()

    def __init__(self, command):
        if command == "test1":
            print("Test One: Warrior v Goblin")
            self.playerOne = Warrior(1)
            self.playerTwo = Goblin(1)
            #print(self.playerTwo.act.prof)
            #for x in self.playerTwo.act.prof:
            #    z = x.getAbl()
            #    y = z.getFx()
            #    print(y)
            #    print(y.getName())
            #    print(str(y.getPow()))
        return

    def step(self):
        input("")
        r = self.d.roll(20)
        print("Roll is " + str(r))
        if self.state == 0:
            abilities = self.playerOne.goRoll(r)
            for a in abilities:
                print(a)
                print("PlayerOne uses ability " + a.getVerb() + "!")
                x = a.getFx()
                print(x)
                print("PlayerOne " + x.getName() + "s for " + str(x.getPow()))
                self.playerTwo.addFx(x)
            self.state = 1
        elif self.state == 1:
            abilities = self.playerTwo.goRoll(r)
            print(abilities)
            for a in abilities:
                print(a)
                print("PlayerTwo uses ability " + a.getVerb() + "!")
                x = a.getFx()
                print(x)
                print("PlayerTwo " + x.getName() + "s for " + str(x.getPow()))
                self.playerOne.addFx(x)

            self.playerTwo.takeEffect()
            self.playerOne.takeEffect()
            self.state = 0
        return

    def run(self):
        while(self.playerOne.isAlive() and self.playerTwo.isAlive()):
            self.step()

        if(self.playerOne.isAlive()):
            "Player One Wins"
        elif(self.playerTwo.isAlive()):
            "Player Two Wins"
        else:
            "???"
        return
