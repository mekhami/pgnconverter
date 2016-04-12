class Game(object):
    def __init__(self, pgn):
        self.pgn = pgn
        self.headers = {}

        self.set_headers()

    def move_list(self):
        with open(self.pgn) as f:
            return f.readlines()[8]

    def set_headers(self):
        with open(self.pgn) as f:
            for line in f.readlines()[0:7]:
                trimmed_line = line[1:-1]  # Get rid of brackets
                param, value = trimmed_line.split(" ")
                self.headers[param] = value
