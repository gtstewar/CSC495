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
        self.deck = Deck.deck(True)
        # print (len(self.deck.facedown))
        # for card in self.deck.facedown:
        #     print(card.value)
        #     print(card.suit)
        self.inPlay = True
        self.winner = None


class GoFish(Game):
    def __init__(self, players, computers):
        print('Welcome to GoooooooooFish')
        print('---------------------------------------------------------------')
        super().__init__(players, computers)
        for i in range(0, players):
            self.players.append(GoFishPlayer(False, i))
        for i in range(0, computers):
            self.players.append(GoFishPlayer(True, i))
        self.playerCount = len(self.players)

    def getPlayerChoicesAndPrint(self, player):
        choicesDic = {}
        iterator = 1
        for p in self.players:
            if not p.__eq__(player):
                choicesDic[iterator] = p
                iterator += 1

        for k in choicesDic.keys():
            print(str(k) + ' ' + choicesDic[k].name)

        return choicesDic

    def ask(self, player, otherPlayer, cardRank):
        print('Asking ' + otherPlayer.name + ' for card...')
        if otherPlayer.checkForCardByRank(cardRank):
            cardsReceived = otherPlayer.giveUpAllCardsByRank(cardRank)
            for c in cardsReceived:
                player.hand.append(c)
            print("Player " + otherPlayer.name + " has given you " + str(len(cardsReceived)) + " of Rank " + str(cardRank.name))
        else:
            print("Player " + otherPlayer.name + " does not have the card you asked for. Go fish!")
            drawn = self.deck.drawCardFromTopOfDeck()
            player.hand.append(drawn)
            print("You have drawn " + drawn.value.name + ' of ' +  drawn.suit.name + " from the deck.")

    def turn(self, player):
        turnString = '\n' + player.name + '\'s turn'
        print(turnString)
        print('********************************')
        player.displayHand()
        print("Which card would you like to ask for? (Please type the number beside the card you want to ask for (Ex: 1))")
        print('>')
        want = sys.stdin.readline()
        want = int(want)
        while (want < 1) or (want > len(player.hand)):
            print('choice must be a card that is in your hand')
            want = sys.stdin.readline
        want = player.hand[want - 1].value
        print("Who would you like to ask? (Please type a number)")
        otherPlayers = self.getPlayerChoicesAndPrint(player)
        print('>')
        who = sys.stdin.readline()
        who = int(who)
        # error checking
        while who not in otherPlayers.keys():
            print("Invalid player. Please enter the number of the player you would like to ask.")
            print('>')
            who = sys.stdin.readline()
        otherPlayer = otherPlayers[who]
        self.ask(player, otherPlayer, want)
        player.sortHandByRank()

        # removes any books in hand
        player.checkForBook()

        if player.isEmptyHand():
            print("You win!!!")
            self.inPlay = False
        else:
            print('Your hand is now:')
            player.displayHand()


    def run(self):
        # Deal cards
        for i in range(self.playerCount):
            for j in range(5):  # each player gets 5 cards
                self.players[i].hand.append(self.deck.drawCardFromTopOfDeck())

        for p in self.players:
            p.sortHandByRank()
        while self.inPlay:
            for i in range(self.playerCount):
                self.turn(self.players[i])
                if not self.inPlay:
                    return self.players[i]
