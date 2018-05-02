from src.GoFish import Deck
from src.GoFish.player import *
import random
#march 17
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Game():
    def __init__(self, players, computers):
        self.maxplayers = 4
        if (players + computers) > self.maxplayers:
            raise Exception("There can only be " + str(self.maxplayers) + " players")
        if (players + computers) <= 1:
            raise Exception("Must have at least 2 players")
        self.players = []
        self.deck = Deck.deck(True)
        # print (len(self.deck.facedown))
        # for card in self.deck.facedown:
        #     print(card.value)
        #     print(card.suit)
        self.inPlay = True


class GoFish(Game):
    def __init__(self, players, computers):
        print('Welcome to GoooooooooFish')
        print('---------------------------------------------------------------')
        super().__init__(players, computers)
        for i in range(0, players):
            self.players.append(GoFishPlayer(False, i, 0))
        for i in range(0, computers):
            self.players.append(GoFishPlayer(True, i, 0))
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

    def computerTurn(self, player):
        turnString = '\n' + player.name + '\'s turn'
        print(turnString)
        print('********************************')
        if player.isEmptyHand():
            print("You have no cards to play! Drawing one card from the top of the deck...")
            player.hand.append(self.deck.drawCardFromTopOfDeck())
        player.displayHand()
        print("Which card would you like to ask for? (Please type the number beside the card you want to ask for (Ex: 1))")
        print('>')
        want = player.computerPickACard()
        print("Who would you like to ask? (Please type a number)")
        otherPlayers = self.getPlayerChoicesAndPrint(player)
        print('>')
        who = random.randint(1, len(self.players) - 1)
        # error checking
        otherPlayer = otherPlayers[who]
        self.ask(player, otherPlayer, want)
        player.sortHandByRank()

        # removes any books in hand
        player.checkForBook()

        # Empty deck: END OF GAME
        if self.deck.isEmpty():
            print("The draw pile is now empty.")
            self.inPlay = False

            # find players' max number of books
            max = 0
            winners = []
            for i in range(self.playerCount):
                if self.players[i].num_books > max:
                   max = self.players[i].num_books
            # check for a tie
            for i in range(self.playerCount):
                if self.players[i].num_books == max:
                    winners.append(self.players[i])
                #announce the winner(s)
                names = []
                for w in winners:
                    names.append(w.name)
            print(str(names) + " have " + str(max) + " book(s). " + str(names) + " win!")

    def turn(self, player):
        turnString = '\n' + player.name + '\'s turn'
        print(turnString)
        print('********************************')
        if player.isEmptyHand():
            print("You have no cards to play! Drawing one card from the top of the deck...")
            player.hand.append(self.deck.drawCardFromTopOfDeck())
        player.displayHand()
        print("Which card would you like to ask for? (Please type the number beside the card you want to ask for (Ex: 1))")
        print('>')
        want = sys.stdin.readline()
        while not RepresentsInt(want):
            print('input must be numeric value...try again\n>')
            want = sys.stdin.readline()
        want = int(want)
        while (want < 1) or (want > len(player.hand)):
            print('choice must be a card that is in your hand')
            while not RepresentsInt(want):
                print('input must be numeric value...try again\n>')
                want = sys.stdin.readline()
            want = int(want)
        want = player.hand[want - 1].value
        print("Who would you like to ask? (Please type a number)")
        otherPlayers = self.getPlayerChoicesAndPrint(player)
        print('>')
        who = sys.stdin.readline()
        while not RepresentsInt(who):
            print('input must be numeric value...try again\n>')
            who = sys.stdin.readline()
        who = int(who)
        # error checking
        while who not in otherPlayers.keys():
            print("Invalid player. Please enter the number of the player you would like to ask.")
            print('>')
            who = sys.stdin.readline()
            while not RepresentsInt(who):
                print('input must be numeric value...try again\n>')
                who = sys.stdin.readline()
            who = int(who)
        otherPlayer = otherPlayers[who]
        self.ask(player, otherPlayer, want)
        player.sortHandByRank()

        # removes any books in hand
        player.checkForBook()

        # Empty deck: END OF GAME
        if self.deck.isEmpty():
            print("The draw pile is now empty.")
            self.inPlay = False

            # find players' max number of books
            max = 0
            winners = []
            for i in range(self.playerCount):
                if self.players[i].num_books > max:
                   max = self.players[i].num_books
            # check for a tie
            for i in range(self.playerCount):
                if self.players[i].num_books == max:
                    winners.append(self.players[i])
                #announce the winner(s)
                names = []
                for w in winners:
                    names.append(w.name)
            print(str(names) + " have " + str(max) + " book(s). " + str(names) + " win!")
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
                if self.players[i].ai:
                    self.computerTurn(self.players[i])
                else:
                    self.turn(self.players[i])
                if not self.inPlay:
                    return self.players[i]
