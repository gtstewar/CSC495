import random
from enum import Enum
import time


class Suit(Enum):
    """
    Suit start from 0 to 3
    """
    Spades = 0
    Hearts = 1
    Clubs = 2
    Diamonds = 3


class Value(Enum):
    """
    Value start from 1 to 13
    """
    Ace, Two, Three, Four = 1, 2, 3, 4
    Five, Six, Seven, Eight = 5, 6, 7, 8
    Nine, Ten, Jack, Queen, King = 9, 10, 11, 12, 13


class Card:
    """
    Card with 2 parameters `suit` and `value`
    """
    def __init__(self, suit, value):
        self.suit = Suit(suit)
        self.value = Value(value)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __repr__(self):
        return str(self.suit) + " and " + str(self.value)


class Deck:
    def __init__(self, is_random_deck, seed_init=time.time()):
        random.seed(seed_init)
        self.face_down = [Card(i, j)
                          for i in range(0, 4)
                          for j in range(1, 14)]
        if is_random_deck:
            random.shuffle(self.face_down)
        self.face_up = []

    def shuffle_current_deck(self):
        random.shuffle(self.face_down)

    def draw_card_from_deck_top(self, left_one=False):
        if self.face_down.__len__() == 0:
            if left_one:
                self.face_down.append(self.face_up.pop())
                random.shuffle(self.face_up)
                self.face_up, self.face_down = self.face_down, self.face_up
            else:
                random.shuffle(self.face_up)
                self.face_down, self.face_up = self.face_up, []
        card = self.face_down.pop()
        return card

    def get_discard_pile_top(self):
        return self.face_up[self.face_up.__len__() - 1]

    def place_card_on_discard_pile(self, card):
        self.face_up.append(card)
