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

class SnipSnapSnoremPlayer(Player):
    def __init__(self, isAI, number, name):
        super(SnipSnapSnoremPlayer, self).__init__(isAI, number, name)

    def computerPickACard(self):
        rank = None
        card = None
        maxCount = 0
        for i in range(1, 14):
            count = 0
            for c in self.hand:
                if c.value.value == rank:
                    count += 1
                if count > maxCount:
                    card = c
                    maxCount = count
        if card is not None:
            return card
        return self.hand[0]

    def sortHandByRank(self):
        self.hand.sort()

    def checkForCard(self, card):
        for c in self.hand:
            if c.value == card.value and c.suit == card.suit:
                return True
        return False

    def checkForCardByRank(self, cardRank):
        for c in self.hand:
            # print("Checking...")
            # print("c.value: " + str(c.value))
            # print("cardRank: " + str(cardRank))
            if c.value == cardRank:
                return True
        return False

    def getCardToStart(self):
        startingCard = self.hand[0]
        self.hand.remove(startingCard)
        return startingCard

    def giveUpCardByRank(self, cardRank):
        ret = []
        # adds cards to be given up
        for c in self.hand:
            if c.value == cardRank:
                ret.append(c)
                break
        # updates self.hand to have cards not in cardThatMatch
        self.hand = [c for c in self.hand if c not in ret]
        return ret[0]

    def isEmptyHand(self):
        if len(self.hand) == 0:
            return True
        else:
            return False