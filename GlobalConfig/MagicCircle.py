from DeckConfig import *
from PlayerConfig import *


class MCEnv(object):
    def __init__(self, player_ls, is_win):
        self.players = player_ls
        self.face_down = Deck()
        self.face_up = FaceUp()
        self.current_player = 0
        self.winner = None
        self.check_is_win = is_win

    def next_player(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player %= len(self.players)

    def start_env(self):
        for i in self.players:
            if not isinstance(i, Player):
                raise TypeError
        for _ in range(5):
            for j in self.players:
                j.get(self.face_down.extract())
