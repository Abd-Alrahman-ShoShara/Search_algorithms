from Iron import Iron
from Magnet import Magnet
from Game import Game

class dfs_solver:
    def __init__(self, game):
        self.game= game
        self.viseted = set()

    def try_dfs(self):
        initial_State=self.game.grid
        path=[]

    def dfs(self, current_state,path):
        if current_state in self.viseted:
            return False
        self.viseted.add(current_state)
        if self.game.check_win():
            return True
        the_magnets = self.game.get_all_magnets()

        for dx , dy in [(-1 ,0),(1,0),(0,-1),(0,1)]:
            new_x,new_y= the_magnets.x + dx , the_magnets.y+dy

            if 0 <= new_x < self.game.grid.width and 0 <= new_y < self.game.grid.height:
                old_state = self.save_state()




    def save_state(self):
        state=[]

        for x in self.game.grid:
            for y in self.game.grid:
                for obj in x:
                    state.append(obj ,obj.x,obj.y)
        return state       