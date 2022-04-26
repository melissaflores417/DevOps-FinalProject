import unittest
from poker_game import play_game
from player import Player
from hand import Hand

class testGame(unittest.TestCase):
    def setUp(self):
        self.game = play_game()

# Test interaction between the player and hand class
