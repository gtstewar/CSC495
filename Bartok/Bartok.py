from Util import *
from random import shuffle


class Bartok:
    def __init__(self, people_array):
        if list(people_array).__len__() > 4:
            raise Exception("More than 4 players")
        self.deck = Deck(True)
        self.player_list = []
        self.player_list += list(map(lambda x: Player(x), people_array))
        self.player_list += list(map(lambda x: Player("An AI Player " + str(x), True),
                                 list(range(4 - list(people_array).__len__()))))
        shuffle(self.player_list)
        for _ in range(5):
            for i in self.player_list:
                i.receive_card(self.deck.draw_card_from_top_of_deck())

    def run(self):
        pass
