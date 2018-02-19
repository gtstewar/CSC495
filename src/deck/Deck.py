import random
from enum import Enum


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


class deck:
    def __init__(self, randomDeck):
        self.facedown = [Card(i, j) for i in range(0, 4) for j in range(1, 14)]
        if randomDeck:
            self.facedown = random.shuffle(self.facedown)
        self.faceup = []

    def shuffleCurrentDeck(self):
        self.facedown = random.shuffle(self.facedown)

    def drawCardFromTopOfDeck(self):
        if len(self.facedown) == 0:
            self.facedown = random.shuffle(self.faceup)
            self.faceup = []
        card = self.facedown[len(self.facedown - 1)]
        self.facedown[len(self.facedown - 1)] = None
        return card

    def placeTopCardOfDeckOnDiscardPile(self):
        if len(self.facedown) == 0:
            self.facedown = random.shuffle(self.faceup)
            self.faceup = []
        temp = self.facedown[len(self.facedown - 1)]
        self.facedown[len(self.facedown - 1)] = None
        self.faceup.append(temp)

    def getTopCardofDiscardPile(self):
        return self.faceup[len(self.faceup - 1)]

    def placeCardOnDiscardPile(self, card):
        self.faceup.append(card)