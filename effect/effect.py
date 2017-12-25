class Effect:
    'two part tuple describing effect on character'
    name = ""
    power = 0
    time = 1

    def __init__(self, n, p, t):
        self.name = n
        self.power = p
        self.time = t
        return

    def getName(self):
        return self.name

    def getPow(self):
        return self.power

    def tick(self):
        self.time = self.time - 1
        if self.time <= 0:
            return false
        else:
            return true
