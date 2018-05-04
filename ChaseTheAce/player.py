import random


class Player(object):
    def __init__(self, isAI, number, name):
        self.ai = isAI
        self.name = name
        self.number = number
        self.hand = []
        self.num_books = 0

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class ChaseTheAcePlayer(Player):
    def __init__(self, isAI, number, name):
        super(ChaseTheAcePlayer, self).__init__(isAI, number, name)

    def computerPickAChoice(self):
        k = random.randint(0, 1)
        if k == 0:
            return "stand"
        else:
            return "change"

    def sortHandByRank(self):
        self.hand.sort()

    def checkForCard(self, card):
        for c in self.hand:
            if c.value == card.value and c.suit == card.suit:
                return True
        return False

    def checkForCardByRank(self, cardRank):
        for c in self.hand:
            if c.value == cardRank:
                return True
        return False

    def getCardToStart(self):
        startingCard = self.hand[0]
        self.hand.remove(startingCard)
        return startingCard

    def giveCard(self):
        card = self.hand[0]
        # removes card from hand
        self.hand.remove(card)
        # return deleted card
        return card

    def isEmptyHand(self):
        if len(self.hand) == 0:
            return True
        else:
            return False