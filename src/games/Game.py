from ..players.player import *
from ..deck import Deck

class Game():
    def __init__(self, players, computers):
        self.maxplayers = 4
        if (players + computers) > self.maxplayers:
            raise Exception("There can only be " + self.maxplayers + " players")
        if (players + computers) <= 1:
            raise Exception("Must have at least 2 players")
        self.players = []
        self.deck = Deck(True)

class GoFish(Game):
    def __init__(self, players, computers):
        super.__init__(self, players, computers)
        for i in range(0, players):
            self.players.append(GoFishPlayer(False, i))
        for i in range(0, computers):
            self.players.append(GoFishPlayer(True, i))
        self.playerCount = len(players)

    def showOptions(self, currentPlayer):
        print('Ask Player for Card')
        index = 1
        for p in self.players:
            if not p.__eq__(currentPlayer):


    def turn(self, player):
        print(player.name + "'s turn")
        print('---------------------')
        print("Current Hand:\n")
        player.displayHand()
        print("Which card would you like to ask for? (Please type the number from the list of cards)")
        want = sys.stdin.readline
        # do error checking here
        print("Who would you like to ask?")
        who = sys.stdin.readline
        # do error checking here


    def run(self):
        print('Welcome to GoooooooooFish\n')
        inPlay = True
        # Deal cards
        for i in range(self.playerCount):
            for j in range(5):  # each player gets 5 cards
                self.players[i].hand.append(self.deck.drawCardFromTopOfDeck())
        while(inPlay):
            for i in range(self.playerCount):
                self.turn(self.players[i])



