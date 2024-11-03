from math import gamma

from GoalCell import GoalCell
from Grid import Grid
from EmptyCell import  EmptyCell
from Iron import Iron
from Magnet import Magnet


def get_direction(magnet, obj):
    if obj.y < magnet.y:
        return "left"
    elif obj.y > magnet.y:
        return "right"
    elif obj.x < magnet.x:
        return "up"
    elif obj.x > magnet.x:
        return "down"
    return None


class Game:
    def __init__(self, width, height, moves):
        self.grid = Grid(width, height)
        self.moves = moves
        self.visited = set()

    def add_object(self, obj, x, y):
        self.grid.add_object(obj, x, y)

    def get_all_magnets(self):
        magnets = []
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if isinstance(cell, Magnet):
                    magnets.append(cell)
        return magnets
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def move_magnet(self, magnet, new_x, new_y):
        if 0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height:

            target_cell = self.grid.grid[new_x][new_y]

            if (isinstance(target_cell, EmptyCell) and target_cell.state) or \
                    (isinstance(target_cell, GoalCell) and target_cell.state):
                self.moves -= 1

                # Empty the previous cell
                self.grid.add_object(EmptyCell(magnet.x, magnet.y, True), magnet.x, magnet.y)

                # Update magnet position
                magnet.x, magnet.y = new_x, new_y
                self.grid.add_object(magnet, new_x, new_y)

                # Move surrounding objects
                if magnet.type=="N":
                    self.move_objects_around_magnet(magnet)
                else:
                    self.move_objects_around_magnet2(magnet)


                # the_bord= self.grid
                # return the_bord
                # self.print_grid()
                if self.check_win():
                    print("Congratulations! You won by filling all target cells.")
                elif self.check_lose():
                    print("No moves left. You lost.")
                else:
                    print("You haven't won yet.")
            else:
                print("Invalid move. Cannot move to the new location.")
        else:
            print("The new location is outside the grid boundaries.")

    def move_magnet_for_dfs(self, magnet, new_x, new_y):
        if 0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height:

            target_cell = self.grid.grid[new_x][new_y]

            if (isinstance(target_cell, EmptyCell) and target_cell.state) or \
                    (isinstance(target_cell, GoalCell) and target_cell.state):
                self.moves -= 1

                # Empty the previous cell
                self.grid.add_object(EmptyCell(magnet.x, magnet.y, True), magnet.x, magnet.y)

                # Update magnet position
                magnet.x, magnet.y = new_x, new_y
                self.grid.add_object(magnet, new_x, new_y)

                # Move surrounding objects
                if magnet.type == "N":
                    self.move_objects_around_magnet(magnet)
                else:
                    self.move_objects_around_magnet2(magnet)

                the_bord= self.grid
                return the_bord
                # self.print_grid()
                # if self.check_win():
                #     print("عاااش لقد حققت الفوز بجعل جميع خلايا الهدف ممتلئة.")
                # elif self.check_lose():
                #     print("لم يتبق لديك أي تحركات. لقد خسرت")
                # else:
                #     print("لم يتم تحقيق الفوز بعد.")
            else:
                print("Invalid move. The new location is not suitable.")
        else:
            print("the new location is out of the grid")
    def check_win(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if isinstance(cell, GoalCell) and not isinstance(self.grid.grid[x][y], (Magnet, Iron)):
                    return False
        return True

    def check_lose(self):
        if self.moves <= 0:
            return True
        else:
            return False

    # def get_All_objects_around(self, magnet):
    #     x, y = magnet.x, magnet.y
    #     objects_around = []
    #
    #     for dx in range(self.grid.width):
    #         if dx != x:
    #             cell = self.grid.grid[y][dx]
    #             if isinstance(cell, (Iron, Magnet)):
    #                 objects_around.append(cell)
    #
    #     for dy in range(self.grid.height):
    #         if dy != y:
    #             cell = self.grid.grid[dy][x]
    #             if isinstance(cell, (Iron, Magnet)):
    #                 objects_around.append(cell)
    #
    #     return objects_around

    def get_objects_around(self, magnet):
        x, y = magnet.x, magnet.y
        objects_around = []

        # right of the magnet
        for dy in range(y + 1, self.grid.width):
            cell = self.grid.grid[x][dy]
            if isinstance(cell, (Iron, Magnet)):
                objects_around.append(cell)
                break

        # left of the magne
        for dy in range(y - 1, -1, -1):
            cell = self.grid.grid[x][dy]
            if isinstance(cell, (Iron, Magnet)):
                objects_around.append(cell)
                break

        # down
        for dx in range(x + 1, self.grid.height):
            cell = self.grid.grid[dx][y]
            if isinstance(cell, (Iron, Magnet)):
                objects_around.append(cell)
                break

        # up
        for dx in range(x - 1, -1, -1):
            cell = self.grid.grid[dx][y]
            if isinstance(cell, (Iron, Magnet)):
                objects_around.append(cell)
                break

        return objects_around

    def move_objects_around_magnet2(self, magnet):
        x, y = magnet.x, magnet.y


        #left
        for dy in range(y - 1, -1, -1):
            cell = self.grid.grid[x][dy]
            if isinstance(cell, (Iron, Magnet)):
                new_x, new_y = x, dy + 1
                if self.is_valid_move(new_x, new_y):
                    self.try_move_object(cell, new_x, new_y)

        # right
        for dy in range(y + 1, self.grid.width):
            cell = self.grid.grid[x][dy]
            if isinstance(cell, (Iron, Magnet)):
                new_x, new_y = x, dy - 1
                if self.is_valid_move(new_x, new_y):
                    self.try_move_object(cell, new_x, new_y)

        #  column
        # above
        for dx in range(x - 1, -1, -1):
            cell = self.grid.grid[dx][y]
            if isinstance(cell, (Iron, Magnet)):
                new_x, new_y = dx + 1, y
                if self.is_valid_move(new_x, new_y):
                    self.try_move_object(cell, new_x, new_y)
        #  below
        for dx in range(x + 1, self.grid.height):
            cell = self.grid.grid[dx][y]
            if isinstance(cell, (Iron, Magnet)):
                new_x, new_y = dx - 1, y
                if self.is_valid_move(new_x, new_y):
                    self.try_move_object(cell, new_x, new_y)

    def is_valid_move(self, new_x, new_y):
        if 0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height:
            target_cell = self.grid.grid[new_x][new_y]
            return isinstance(target_cell, (EmptyCell, GoalCell)) and target_cell.state
        return False

    def move_objects_around_magnet(self, magnet):
        if magnet.type == "N":
            objects_around = self.get_objects_around(magnet)
            for obj in objects_around:
                direction = get_direction(magnet, obj)
                self.move_object_towards_magnet(obj, direction)

        # if magnet.type == "S":
        #     objects_aroundw = self.get_All_objects_around(magnet)
        #     for obj in objects_aroundw:
        #         direction = get_direction(magnet, obj)
        #         self.move_object_away_from_magnet(obj, direction)

    def move_object_towards_magnet(self, obj, direction):
        self.move_object(obj, direction, towards=True)

    def move_object_away_from_magnet(self, obj, direction):
        self.move_object(obj, direction, towards=False)

    def move_object(self, obj, direction, towards):
        dx, dy = 0, 0
        if direction == "left":
            dy = -1 if towards else 1

        elif direction == "right":
            dy = 1 if towards else -1

        elif direction == "up":
            dx = -1 if towards else 1

        elif direction == "down":
            dx = 1 if towards else -1

        next_x, next_y = obj.x + dx, obj.y + dy

        if 0 <= next_x < self.grid.width and 0 <= next_y < self.grid.height:
            target_cell = self.grid.grid[next_x][next_y]


            if (isinstance(target_cell, EmptyCell) and target_cell.state) or \
                    (isinstance(target_cell, GoalCell) and target_cell.state):
                self.try_move_object(obj, next_x, next_y)


            elif isinstance(target_cell, (Iron, Magnet)):
                next_x2, next_y2 = next_x + dx, next_y + dy


                if 0 <= next_x2 < self.grid.width and 0 <= next_y2 < self.grid.height:
                    second_target_cell = self.grid.grid[next_y2][next_x2]


                    if (isinstance(second_target_cell, EmptyCell) and second_target_cell.state) or \
                            (isinstance(second_target_cell, GoalCell) and second_target_cell.state):

                        self.try_move_object(target_cell, next_x2, next_y2)

                        self.try_move_object(obj, next_x, next_y)

    def try_move_object(self, obj, new_x, new_y):
        target_cell = self.grid.grid[new_x][new_y]
        if isinstance(target_cell, (EmptyCell, GoalCell)) and target_cell.state:
            self.grid.add_object(EmptyCell(obj.x, obj.y, True), obj.x, obj.y)
            obj.x, obj.y = new_x, new_y
            self.grid.add_object(obj, new_x, new_y)

    def print_grid(self):
        print("Grid:")
        for y in range(self.grid.height):
            row = []
            for x in range(self.grid.width):
                cell = self.grid.grid[y][x]
                row.append(cell.display() if hasattr(cell, "display") else "EmptyCell")
            print(" | ".join(row))
            print("-" * (self.grid.width * 12))

    def play(self):
        while self.moves > 0 and not self.check_win():
            try:
                self.print_grid()

                # Get all magnets from the grid
                magnets = self.get_all_magnets()
                if not magnets:
                    print("there is no magnets.")
                    return


                print("Available Magnets:")
                for index, magnet in enumerate(magnets):
                    print(f"{index + 1}. Magnet at ({magnet.y}, {magnet.x}) type {magnet.type}")

                # Let user select a magnet
                magnet_choice = int(input("Enter the number of the magnet you want to move: ")) - 1
                if magnet_choice < 0 or magnet_choice >= len(magnets):
                    print("اختيار غير صالح.")
                    continue

                selected_magnet = magnets[magnet_choice]


                new_x = int(input("Enter the new X coordinate for the magnet: "))
                new_y = int(input("Enter the new Y coordinate for the magnet: "))
                self.move_magnet(selected_magnet, new_x, new_y)

            except ValueError:
                print("please enter a  number.")

    def clear_movable_objects(self):
        for row in self.grid.grid:
            for obj in row:
                if isinstance(obj, (Magnet, Iron)):
                    self.grid.remove_object(obj)


    # def play_game(self, magnet):
    #     choice = input("اختر وضع اللعبة:\n1. اللعب اليدوي\n2. الحل التلقائي\n")
    #     if choice == '1':
    #         self.play(magnet)
    #     elif choice == '2':
    #         method = input("اختر الخوارزمية لحل اللعبة:\n1. DFS\n2. BFS\n")
    #         if method == '1':
    #             self.play_dfs(magnet)
    #
    #         elif method == '2':
    #             solution_path = self.bfs(magnet)
    #             if solution_path:
    #                 print("الحل باستخدام BFS: ")
    #                 for step in solution_path:
    #                     print("خطوة:", step)
    #             else:
    #                 print("لم يتم العثور على حل باستخدام BFS.")
    #     else:
    #         print("اختيار غير صالح.")

