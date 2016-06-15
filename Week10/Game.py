"""
Game - represents the state of game-play of our guessing game
"""

from random import randint


class Game:
    def __init__(self):
        self.secret = 0
        self.number_of_moves = 0
        self.set_secret()

    def set_secret(self):
        self.secret = randint(0, 11)

    def guess(self, value):
        if value > self.secret:
            return 'try smaller'
        elif value < self.secret:
            return 'try bigger'
        else:
            self.number_of_moves = -1
            self.set_secret()
            return 'found it'

    def add_move(self):
        self.number_of_moves += 1
        return self.number_of_moves