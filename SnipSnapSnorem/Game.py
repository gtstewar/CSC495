
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

class SnipSnapSnorem(Game):

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
        # if the card exists in hand, give up the card and add to top of discard pile
        receivedCards = 0
        if player.checkForCardByRank(card.value):
            # gives up 1 card with same rank as top of discard pile
            received = player.giveUpCardByRank(card.value)
            # and places it on top of the discard pile
            self.environment.deck.placeCardOnDiscardPile(received)
            print("You have a match! Placing your card on top of the pile.")
        else:
            print("You don't have any matches for this turn! :(")
            receivedCards = -1
        self.environment.currentPlayer.sortHandByRank()
        return receivedCards

    def setUp(self):
        numPlayers = len(self.environment.players)
        numCards = int(52 / numPlayers)
        for player in self.environment.players:
            for i in range(numCards):
                player.hand.append(self.environment.deck.drawCardFromTopOfDeck())

    def firstCardOnDiscardPile(self, card):
        self.environment.deck.placeCardOnDiscardPile(card)

    def getFirstCardOnDiscardPile(self):
        print("returned from getFirstCardOnDiscardPile: " + str(self.environment.deck.getTopCardofDiscardPile()))
        return self.environment.deck.getTopCardofDiscardPile()

