class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"Stone at ({self.x}, {self.y})"
