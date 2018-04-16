from DeckConfig import Pile
from Rules import *


class Player(Pile):
    def __init__(self, name, self_func):
        super(Player, self).__init__([])
        self.name = name
        self.func = self_func

    @classmethod
    def play(cls, *info):
        pass


# We need to use monad to pass information and state with result
# Since Most Monad are not implemented, i use List as monad
# Since List itself can be considered as a monad

class BartokPlayer(Player):
    def play(self, *info):
        if len(info) != 1:
            raise SyntaxError
        print "<" + self.name + ">" + " met this card: "
        print_formatted(show % info[0])
        print "<" + self.name + ">" + " have these cards: "
        print_formatted(hand_show % L[self.cards])
        toss, self.cards = self.func(L[self.cards], info[0])
        self.cards = [i for i in self.cards]
        if len(toss) != 0:
            print "<" + self.name + ">" + " tossed this:"
            print_formatted(hand_show % toss)
        else:
            print "<" + self.name + ">" + " tossed nothing"
        return toss


# a = BartokPlayer("Anthony", bartok_rule_player)
# a.get(CD(Spade, Ten))
# a.get(CD(Spade, Nine))
# a.get(CD(Spade, Eight))
# a.get(CD(Diamond, King))
# a.play(CD(Diamond, Four))
