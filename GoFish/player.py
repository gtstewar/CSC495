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

class GoFishPlayer(Player):
    def __init__(self, isAI, number, name):
        super(GoFishPlayer, self).__init__(isAI, number, name)

    def computerPickAPlayer(self, env):
        player = None
        while player is None or player == self:
            player = env.players[random.randrange(0,len(env.players))]
        return player

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
            if c.value == cardRank:
                return True
        return False

    def giveUpAllCardsByRank(self, cardRank):
        cardsThatMatch = []
        # adds cards to be given up
        for c in self.hand:
            if c.value == cardRank:
                cardsThatMatch.append(c)
        # updates self.hand to have cards not in cardThatMatch
        self.hand = [c for c in self.hand if c not in cardsThatMatch]
        return cardsThatMatch

    def checkForBook(self):
        for i in range(1, 14):
            count = 0
            for c in self.hand:
                if c.value.value == i:
                    count += 1
                    if count == 4:
                        for ca in reversed(self.hand):
                            if ca.value.value == i:
                                self.hand.remove(ca)
                       # self.hand[:] = [x for x in self.hand if not c.value.value]
                        self.num_books += 1
                        return True
        return False

    def isEmptyHand(self):
        if len(self.hand) == 0:
            return True
        else:
            return False