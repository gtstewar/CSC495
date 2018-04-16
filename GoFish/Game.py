
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Game():
    def __init__(self, environment):
        self.environment = environment

    def switchTurns(self):
        for i in range(len(self.environment.players)):
            if self.environment.players[i] == self.environment.currentPlayer:
                if i == (len(self.environment.players) - 1):
                    self.environment.currentPlayer = self.environment.players[0]
                    break
                else:
                    self.environment.currentPlayer = self.environment.players[i + 1]
                    break

class GoFish(Game):

    def validCardInput(self, card):
        if not RepresentsInt(card):
            return False
        card = int(card)
        if card < 1 or card > len(self.environment.currentPlayer.hand):
            return False
        return True

    def validPlayerInput(self, player):
        if not RepresentsInt(player):
            return False
        player = int(player)
        if player < 1 or player >= len(self.environment.players):
            return False
        return True

    def receivePlayer(self):
        if not self.environment.currentPlayer.ai:
            p = input()
            if not self.validPlayerInput(p):
                return None
            else:
                p = int(p)
                i = 1
                for player in self.environment.players:
                    if player != self.environment.currentPlayer and p == i:
                        return player
                    elif player != self.environment.currentPlayer:
                        i += 1
        return self.environment.currentPlayer.computerPickAPlayer(self.environment)
    def receiveCard(self):
        if not self.environment.currentPlayer.ai:
            card = input()

            if not self.validCardInput(card):
                return None
            else:
                card = int(card)
                return self.environment.currentPlayer.hand[card - 1]
        return self.environment.currentPlayer.computerPickACard()

    def executeTurn(self, card, player):
        receivedCards = 0
        if player.checkForCardByRank(card.value):
            cardsReceived = player.giveUpAllCardsByRank(card.value)
            receivedCards = len(cardsReceived)
            for c in cardsReceived:
                self.environment.currentPlayer.hand.append(c)
        else:
            self.environment.currentPlayer.hand.append(self.environment.deck.drawCardFromTopOfDeck())
        self.environment.currentPlayer.sortHandByRank()
        return receivedCards

    def findWinners(self):
        highestBooks = 0
        for player in self.environment.players:
            if player.num_books > highestBooks:
                highestBooks = player.num_books

        for player in self.environment.players:
            if player.num_books == highestBooks:
                self.environment.winners.append(player)

    def setUp(self):
        for player in self.environment.players:
            for i in range(5):
                player.hand.append(self.environment.deck.drawCardFromTopOfDeck())


