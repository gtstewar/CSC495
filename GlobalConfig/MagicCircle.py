from DeckConfig import *


class MCEnv(object):
    def __init__(self, player_ls, is_win):
        self.players = player_ls
        self.face_down = Deck()
        self.face_up = FaceUp()
        self.current_player = 0
        self.winner = None
        self.check_is_win = is_win
