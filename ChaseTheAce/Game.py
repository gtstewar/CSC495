
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
                   # self.environment.previousPlayer = self.environment.players[len(self.environment.players) - 1]
                    self.environment.nextPlayer = self.environment.players[1]
                    self.environment.nextNextPlayer = self.environment.players[2]
                    break
                else:
                    self.environment.currentPlayer = self.environment.players[i + 1]
                    # self.environment.previousPlayer = self.environment.players[i]
                    self.environment.nextPlayer = self.environment.players[i + 2]
                    self.environment.nextNextPlayer = self.environment.players[i + 3]
                    break

class ChaseTheAce(Game):

    def receiveChoice(self):
        if not self.environment.currentPlayer.ai:
            choice = input()
            return str(choice)
        return str(self.environment.currentPlayer.computerPickAChoice())

    def executeTurn(self, choice, nextPlayer):
        # if the player chooses "change", swap cards with next player.
        if choice == "change":
            if nextPlayer.hand[0].value != 13:
                # get current player's card to give up
                cardToGiveUp1 = self.environment.currentPlayer.giveCard()
                # get next player's card to give up
                cardToGiveUp2 = nextPlayer.giveCard()
                # current player gets new card
                self.environment.currentPlayer.hand.append(cardToGiveUp2)
                # next player gets new card
                nextPlayer.hand.append(cardToGiveUp1)
            else:
                print(self.environment.nextPlayer.name + "has a King! Switching with next player...")
                executeTurn(choice, self.environment.nextNextPlayer)
        # if the player chooses "stand", do nothing. end of turn.

    def setUp(self):
        # each player gets a single card
        for player in self.environment.players:
            player.hand.append(self.environment.deck.drawCardFromTopOfDeck())


    def firstCardOnDiscardPile(self, card):
        self.environment.deck.placeCardOnDiscardPile(card)

    def getFirstCardOnDiscardPile(self):
        return self.environment.deck.getTopCardofDiscardPile()

    def findWinners(self):
        for player in self.environment.players:
            if player.isEmptyHand():
                self.environment.winners.append(player)

