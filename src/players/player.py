class Player():
    def __init__(self, name, isAI):
        self.ai = isAI
        self.name = name
        self.hand = []

    def displayHand(self):
        print("current hand")
        print("------------")
        counter = 1
        for card in self.hand:
            if counter % 3 == 0:
                print('\n')
            counter += 1
            print(self.hand.value + " of " + self.hand.suit)
        print("------------")

    def run(self):
        return 0

class goFishPlayer(Player):
    def checkForCard(self, card):
        for c in self.hand:
            if c.value == card.value and c.suit == card.suit:
                self.hand.remove(c)
                return True
        return False
