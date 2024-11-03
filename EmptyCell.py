from Cell import Cell
class EmptyCell(Cell):
    def __init__(self, x, y, state=True):
        super().__init__(x, y)
        self.state = state

    def display(self):
        return f"EmptyCell "
