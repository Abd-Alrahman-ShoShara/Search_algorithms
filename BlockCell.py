from Cell import Cell
class BlockCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def display(self):
        return f"BlockCell"

