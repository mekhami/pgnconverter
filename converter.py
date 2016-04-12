class Game(object):
    def __init__(self, pgn):
        self.pgn = pgn

    def move_list(self):
        with open(self.pgn) as f:
            return f.readlines()[8]
