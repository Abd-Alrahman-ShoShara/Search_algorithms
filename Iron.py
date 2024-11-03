from Stone import Stone

class Iron(Stone):
    def __init__(self, x, y):
        super().__init__(x, y)

    def display(self):
        return f"Iron      "
