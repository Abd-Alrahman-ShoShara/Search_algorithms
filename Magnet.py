from Stone import Stone
class Magnet(Stone):
    def __init__(self, x, y, type):
        super().__init__(x, y)
        self.type = type

    def display(self):
        if self.type=="S":
            return f"S_Magnet  "
        else:
            return f"N_magnet  "
   