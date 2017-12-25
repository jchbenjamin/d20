from random import randint, seed
from datetime import datetime

def checkTwenty(n):
    if n > 20 or n < 1:
        raise Exception('Improper roll count!')
        quit()

class Dice:
    def __init__(self):
        seed(datetime.now())

    def roll(self, n):
        if n in [20, 12, 10, 6, 4, 2]:
            return(randint(1, n))
        else:
            raise Exception('Improper Dice Roll!')
            quit()
