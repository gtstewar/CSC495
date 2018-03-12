from src.games import Deck
from src.games.player import *


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

    # commenting out for now
    # def showOptions(self, currentPlayer):
    #     print('Ask Player for Card')
    #     index = 1
    #     for p in self.players:
    #         if not p.__eq__(currentPlayer):

    def ask(self, player, otherPlayer, card ):
        print('Asking ' + otherPlayer + 'for card...')
        for i in range(self.playerCount):
            if otherPlayer == self.players[i]:
                if self.players[i].checkForCard(self.players[i], card):
                    player.append(card)
                    print("Player " + otherPlayer + " has given you the card.")
                else:
                    print("Player " + otherPlayer + " does not have the card you asked for. Go fish!")
                    player.append(self.deck.drawCardFromTopOfDeck())
                    print("You have drawn a card from the deck.")

    def turn(self, player):
        print(player.name + "'s turn")
        print('---------------------')
        print("Current Hand:\n")
        player.displayHand()


        print("Which card would you like to ask for? (Please type the value and suite of the card separated by a space.")
        print("Example: 1 Hearts")
        want = sys.stdin.readline
        temp = want.split
        want = Deck.Card(temp[0], temp[1])
        # do error checking here



        print("Who would you like to ask? (Please type a number)")
        who = sys.stdin.readline
        # error checking
        while who < 0 or who >= self.playerCount:
            print("Invalid player. Please enter the number of the player you would like to ask.")
            who = sys.stdin.readline
        self.ask(who, want)

        # removes any pairs in hand
        player.checkForPairs()

        if player.isEmptyHand():
            print("You win!")
            # exit game??? idk what happens here

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



