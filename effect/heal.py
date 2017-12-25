from effect.effect import Effect

class Heal(Effect):
    def __init__(self, p):
        Effect.__init__(self, "heal", p, 1)
        return
        
