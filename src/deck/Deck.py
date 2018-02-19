import random

class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class deck:
    def __init(self, randomDeck):
        self.facedown = [card("Spades", "Ace"), card("Spades", "2"), card("Spades", "3"), card("Spades", "4"), card("Spades", "5"), card("Spades", "6"), card("Spades", "7"), card("Spades", "8"), card("Spades", "9"), card("Spades", "10"), card("Spades", "Jack"), card("Spades", "Queen"), card("Spades", "King"), card("Hearts", "Ace"), card("Hearts", "2"), card("Hearts", "3"), card("Hearts", "4"), card("Hearts", "5"), card("Hearts", "6"), card("Hearts", "7"), card("Hearts", "8"), card("Hearts", "9"), card("Hearts", "10"), card("Hearts", "Jack"), card("Hearts", "Queen"), card("Hearts", "King"), card("Clubs", "Ace"), card("Clubs", "2"), card("Clubs", "3"), card("Clubs", "4"), card("Clubs", "5"), card("Clubs", "6"), card("Clubs", "7"), card("Clubs", "8"), card("Clubs", "9"), card("Clubs", "10"), card("Clubs", "Jack"), card("Clubs", "Queen"), card("Clubs", "King"), card("Diamonds", "Ace"), card("Diamonds", "2"), card("Diamonds", "3"), card("Diamonds", "4"), card("Diamonds", "5"), card("Diamonds", "6"), card("Diamonds", "7"), card("Diamonds", "8"), card("Diamonds", "9"), card("Diamonds", "10"), card("Diamonds", "Jack"), card("Diamonds", "Queen"), card("Diamonds", "King")]
        if randomDeck:
            self.facedown = random.shuffle(self.facedown)
        self.faceup = []

    def shuffleCurrentDeck(self):
        self.facedown = random.shuffle(self.facedown)

    def drawCardFromTopOfDeck(self):
        if len(self.facedown) == 0:
            self.facedown = random.shuffle(self.faceup)
            self.faceup = []
        return self.facedown[len(self.facedown - 1)]

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