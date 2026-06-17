class Action: 

    def perform(self):
        pass



class EscapeAction(Action):
    def perform(self):
        raise SystemExit()



class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        
        self.dx = dx
        self.dy = dy
        
    def perform(self):
        pass
        