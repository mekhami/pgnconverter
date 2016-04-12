import unittest

from converter import Game


class PGNConverterTest(unittest.TestCase):
    def setUp(self):
        self.pgn = open("strzeleckiantunes.pgn")
        self.game = Game(self.pgn)
    
    def test_get_move_list(self):
        self.assertIn("1. e4 c5", self.game.move_list)
