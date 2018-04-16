from CardConfig import *
from random import shuffle, seed
from Pyskell import *
from time import time


@TS(C / ["a"] >> ["a"])
def h_shuffle(h_l):
    temp_l = [_i for _i in h_l]
    shuffle(temp_l)
    return L[temp_l]


@TS(C / int >> [Card])
def init_face_down(sd):
    seed(sd)
    unit_lb, unit_hb = bounds % Diamond
    value_lb, value_hb = bounds % Two
    init_list = [CD(_i, j) for _i in L[unit_lb, ..., unit_hb]
                 for j in L[value_lb, ..., value_hb]]
    shuffle(init_list)
    return L[init_list]


class Pile(object):
    def __init__(self, fill_cards):
        self.cards = fill_cards

    def empty(self):
        return self.contain_num() == 0

    def contain_num(self):
        return len(self.cards)

    def extract(self):
        if self.empty():
            raise KeyError("No cards in pile")
        toss, self.cards = ~(CaseOf(self.cards)
                             | pb(pb.x ^ pb.y) >> (va.x, va.y))
        return toss

    def append(self, other):
        if isinstance(other, Pile):
            self.cards = [_i for _i in self.cards] + [_i for _i in other.cards]
        elif isinstance(other, list):
            self.cards = [_i for _i in self.cards] + other
        elif isinstance(other, HaskellList):
            self.cards = [_i for _i in self.cards] + [_i for _i in other]
        elif isinstance(other, Card):
            self.cards.append(other)
        else:
            raise SyntaxError

    def re_shuffle(self):
        temp = [c for c in self.cards]
        shuffle(temp)
        self.cards = temp


class Deck(Pile):
    def __init__(self):
        super(Deck, self).__init__(init_face_down(int(time())))


class FaceUp(Pile):
    def __init__(self):
        super(FaceUp, self).__init__([])
