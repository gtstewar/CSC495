from src.GoFish import Deck
from src.Version2.player import *
import random

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
            if self.environment.players[i].__eq__(self.environment.currentPlayer):
                if i == len(self.environment.players) - 1:
                    self.environment.currentPlayer = self.environment.players[0]
                else:
                    self.environment.currentPlayer = self.environment.players[i + 1]

class GoFish(Game):

    def play(self):
        print('here')

    def validCardInput(self, card):
        if not RepresentsInt(card):
            return False
        card = int(card)
        if card < 0 or card > len(self.environment.currentPlayer.hand):
            return False
        return True

    def validPlayerInput(self, player):
        if not RepresentsInt(player):
            return False
        player = int(player)
        if player < 0 or player > len(self.environment.players) - 1:
            return False
        return True

    def receivePlayer(self):
        if not self.environment.currentPlayer.ai:
            p = input()

        if not self.validPlayerInput(p):
            return None
        else:
            p = int(p)
            return self.environment.players[p]

    def receiveCard(self):
        if not self.environment.currentPlayer.ai:
            card = input()

        if not self.validCardInput(card):
            return None
        else:
            card = int(card)
            return self.environment.currentPlayer.hand[card]

    def executeTurn(self, card, player):
        receivedCards = 0
        if player.checkForCardByRank(card.value):
            cardsReceived = player.giveUpAllCardsByRank()
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


