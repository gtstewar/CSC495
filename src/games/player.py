import sys

class Player():
    def __init__(self, isAI, number):
        self.ai = isAI
        if not self.ai:
            print('Enter your name Player ' + str(number) + ' : ')
            self.name = sys.stdin.readline()
        else:
            self.name = 'Computer ' + str(number)
        self.hand = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def displayHand(self):
        print("Current hand")
        print("------------")
        counter = 1
        for card in self.hand:
            print(str(counter) +  '. ' + card.value.name + " of " + card.suit.name)
            counter += 1
        print("------------")

    def run(self):
        return 0

class GoFishPlayer(Player):
    def __init__(self, isAI, number):
        super().__init__(isAI, number)

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
        for i in range(len(self.hand)):
            c = self.hand[i]
            if c.value == cardRank:
                cardsThatMatch.append(self.hand.pop(i))
        return cardsThatMatch
    """ Checks for pairs in player's hand and removes pairs"""
    def checkForPairs(self):
        for c1 in self.hand:
            for c2 in self.hand:
                if c1 == c2:
                    self.hand.remove(c1)
                    self.hand.remove(c2)
                    break

    def checkForBook(self):
        for i in range(13):
            count = 0
            for c in self.hand:
                if c.value == i:
                    count += 1
                    if count == 4:
                        for k in range(len(self.hand)):
                            if self.hand[k] == i:
                                self.hand.remove(k)
                    return True
        return False
    def isEmptyHand(self):
        if len(self.hand) == 0:
            return True
        else:
            return False