from EmptyCell import EmptyCell
class Grid:

    def __init__(self, width, height ):
        self.width = width
        self.height = height
        self.grid = [[EmptyCell(x, y) for x in range(width)] for y in range(height)]

    def add_object(self, obj, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y] = obj
            obj.x = x
            obj.y = y
        else:
            print(f"Position ({x}, {y}) is out of bounds")


    # def create_grid(self,block_cell,empty_cell,goal_cell,magnet,iron):
    #     self.blockCell = block_cell
    #     self.emptyCell = empty_cell
    #     self.goalCell = goal_cell
    #     self.magnet = magnet
    #     self.iron = iron


