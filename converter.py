class Game(object):
    def __init__(self, pgn):
        self.pgn = open(pgn, "r")

    def move_list(self):
        return self.pgn.readlines()[8]
