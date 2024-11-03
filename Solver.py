from Magnet import Magnet
from Iron import Iron
from Game import Game

class Solver:
    def __init__(self, game):
        self.game = game
        self.visited = set()
