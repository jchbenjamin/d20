from effect.effect import Effect

class Hit(Effect):
    def __init__(self, p):
        Effect.__init__(self, "hit", p, 1)
        return
        
