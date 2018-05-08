from Deck import *
import operator

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Game():
    def __init__(self, environment):
        self.environment = environment
        self.winnerCount = {}
        if len(self.environment.players) == 3:
            self.winnerCount = {self.environment.players[0].name: 0, self.environment.players[1].name: 0,
                                self.environment.players[2].name: 0}
        if len(self.environment.players) == 4:
            self.winnerCount = {self.environment.players[0].name: 0, self.environment.players[1].name: 0,
                                self.environment.players[2].name: 0, self.environment.players[3].name: 0}

    def switchTurns(self):
        if len(self.environment.players) == 3:
            for i in range(len(self.environment.players)):
                if self.environment.players[i] == self.environment.currentPlayer: # old player at index i
                    if i == (len(self.environment.players) - 1):
                        self.environment.currentPlayer = self.environment.players[0]    #new current at beginning
                        self.environment.nextPlayer = self.environment.players[1]
                        self.environment.nextNextPlayer = self.environment.players[2]
                        break
                    else:
                        self.environment.currentPlayer = self.environment.players[i + 1]
                        if i + 1 == (len(self.environment.players) - 1):    #if new current player at end of array
                            self.environment.nextPlayer = self.environment.players[0]
                            self.environment.nextNextPlayer = self.environment.players[1]
                        else:   #new current in middle of array [1]
                            self.environment.nextPlayer = self.environment.players[2]
                            self.environment.nextNextPlayer = self.environment.players[0]
                        break

        elif len(self.environment.players) == 4:
            for i in range(len(self.environment.players)):
                if self.environment.players[i] == self.environment.currentPlayer: #find index of current Player
                    if i == (len(self.environment.players) - 1):
                        self.environment.currentPlayer = self.environment.players[0]    #new current at beginning
                        self.environment.nextPlayer = self.environment.players[1]
                        self.environment.nextNextPlayer = self.environment.players[2]
                        break
                    else:
                        self.environment.currentPlayer = self.environment.players[i + 1]
                        if i + 1 == 3:    #if new current player at end of array
                            self.environment.nextPlayer = self.environment.players[0]
                            self.environment.nextNextPlayer = self.environment.players[1]
                        if i + 1 == 1:
                            self.environment.nextPlayer = self.environment.players[2]
                            self.environment.nextNextPlayer = self.environment.players[3]
                        elif i + 1 == 2:
                            self.environment.nextPlayer = self.environment.players[3]
                            self.environment.nextNextPlayer = self.environment.players[1]
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
            if self.environment.currentPlayer == self.environment.players[-1]: # if last player in list
                card = self.environment.currentPlayer.hand[0]
                # removes card from hand
                self.environment.currentPlayer.hand.remove(card)
                self.environment.currentPlayer.hand.append(self.environment.deck.drawCardFromTopOfDeck())
            else:
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
            if len(player.hand) == 0: #first round, no one has cards
                player.hand.append(self.environment.deck.drawCardFromTopOfDeck())
            else: # subsequent rounds, fresh cards dealt
                del player.hand[0]
                player.hand.append(self.environment.deck.drawCardFromTopOfDeck())

    def firstCardOnDiscardPile(self, card):
        self.environment.deck.placeCardOnDiscardPile(card)

    def getFirstCardOnDiscardPile(self):
        return self.environment.deck.getTopCardofDiscardPile()

    def valueAsInt(self, value):
        if value == Value.Ace: return 1
        if value == Value.Two: return 2
        if value == Value.Three: return 3
        if value == Value.Four: return 4
        if value == Value.Five: return 5
        if value == Value.Six: return 6
        if value == Value.Seven: return 7
        if value == Value.Eight: return 8
        if value == Value.Nine: return 9
        if value == Value.Ten: return 10
        if value == Value.Jack: return 11
        if value == Value.Queen: return 12
        if value == Value.King: return 13

    def findRoundWinner(self):
        winner = None
        totalHigh = Value.Two
        for player in self.environment.players:
            highest = Value.Two #find each player's highest card
            for card in player.hand:
                if self.valueAsInt(card.value) == 1:     # if player has an Ace, they win!
                    winner = player
                    self.winnerCount[winner.name] += 1
                    return winner
                else:
                    if self.valueAsInt(card.value) > self.valueAsInt(highest):
                        highest = card.value
            if self.valueAsInt(highest) > self.valueAsInt(totalHigh): # update winner
                totalHigh = highest
                winner = player
        self.winnerCount[winner.name] += 1
        return winner

    def findOverallWinner(self):
        winners = []
        temp = max(self.winnerCount, key=self.winnerCount.get)
        maxVal = self.winnerCount.get(temp)
        for k, v in self.winnerCount.items():
            if v == maxVal:
                winners.append(k)
        print(str(winners) + " is the overall winner of the game! Congratulations!")


