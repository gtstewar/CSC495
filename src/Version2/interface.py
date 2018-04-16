from src.Version2.Deck import *
import os
from src.Version2.Environment import *
from src.Version2.player import *

class Interface:
    displayValuesRank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    displayValuesSuit = ['S', 'H', 'C', 'D']
    def __init__(self, showComputerTurns, environment):
        self.showComputer = showComputerTurns
        self.environment = environment

    def getCardToDisplay(self, card):
        cardToDisplay = []
        if card.value.value == 10:
            cardToDisplay.append('|{}   |'.format(Interface.displayValuesRank[card.value.value - 1]))
            cardToDisplay.append('|     |')
            cardToDisplay.append('|  {}  |'.format(Interface.displayValuesSuit[card.suit.value]))
            cardToDisplay.append('|     |')
            cardToDisplay.append('|   {}|'.format(Interface.displayValuesRank[card.value.value - 1] ))
        else:
            cardToDisplay.append('|{}    |'.format(Interface.displayValuesRank[card.value.value - 1]))
            cardToDisplay.append('|     |')
            cardToDisplay.append('|  {}  |'.format(Interface.displayValuesSuit[card.suit.value]))
            cardToDisplay.append('|     |')
            cardToDisplay.append('|    {}|'.format(Interface.displayValuesRank[card.value.value - 1]))
        return cardToDisplay

    def clear_screen(self):
        os.system('cls||clear')

    #top half of dash(public information about other players hands)
    def displayOtherPlayersInfo(self):
        print(self.environment.currentPlayer.name + "'s turn")
        #first line - print players names
        print('            ', end = '')
        for player in self.environment.players:
            if self.environment.currentPlayer is not player:
                print(player.name + '   ', end='')
        #print dashed lines under players names
        print('\n            ', end='')
        for player in self.environment.players:
            if self.environment.currentPlayer is not player:
                for i in range(len(player.name)):
                    print('-', end='')
                print('   ', end='')
        #print each players number of cards except for current player
        print('\n# Of Cards  ', end='')
        for player in self.environment.players:
            if self.environment.currentPlayer is not player:
                for i in range(int(len(player.name)/2)):
                    print(' ', end='')
                print(len(player.hand), end='')
                for i in range(int(len(player.name)/2)):
                    print(' ', end='')
                print('   ', end= '')
        #print each players number of books except for current player
        print('\n# Of Books  ', end='')
        for player in self.environment.players:
            if self.environment.currentPlayer is not player:
                for i in range(int(len(player.name)/2)):
                    print(' ', end='')
                print(player.num_books, end='')
                for i in range(int(len(player.name)/2)):
                    print(' ', end='')
                print('   ', end= '')
        #print dashed line underneath provided information
        print('\n')
        lineLength = 12
        lineLength += 3 * (len(self.environment.players) - 1)
        for player in self.environment.players:
            if player is not self.environment.currentPlayer:
                lineLength += len(player.name)
        for i in range(lineLength):
            print('-', end='')
        print('')

    #prints a row of cards
    def printCards(self, rowLength, startNum, cardsToPrint):
        for i in range(5):
            for k in range(rowLength):
                if i == 0:
                    print(str(startNum) + '. ', end='')
                    startNum += 1
                else:
                    print('   ', end='')
                cardToPrint = cardsToPrint[k]
                print(cardToPrint[i] + ' ', end='')
            print('')
        print('')

    #prints the hand plus other relevant information of player (bottom half of the dash)
    def displayCurrentPlayersInfo(self):
        print('Current Hand:')
        cardsToDisplay = []
        i = 1
        total = 1
        for card in self.environment.currentPlayer.hand:
            if i < 6 and total != len(self.environment.currentPlayer.hand):
                cardsToDisplay.append(self.getCardToDisplay(card))
                i += 1
                total += 1
            else:
                self.printCards(i - 1, total - i + 1, cardsToDisplay)
                cardsToDisplay = []
                i = 1
        print('Size of hand ' + str(len(self.environment.currentPlayer.hand )))

    #prints the dashboard for a player given that they arent a computer
    def displayDash(self):
        if not self.environment.currentPlayer.ai or self.showComputer:
            self.clear_screen()
            print()
            self.displayOtherPlayersInfo()
            self.displayCurrentPlayersInfo()

    def promptUserForCard(self):
        if not self.environment.currentPlayer.ai:
            print('Card to Play > ', end='')

    def promptUserForPlayerToAsk(self):
        if not self.environment.currentPlayer.ai:
            i = 1
            for player in self.environment.players:
                if player is not self.environment.currentPlayer:
                    print(str(i) + '. ' + player.name + '  ', end='')
                    i += 1

            print('Who To Ask? > ', end='')

    def displayMessageToUser(self, message):
        print(message)

    def receivedCardsMessage(self, receivedCards):
        if not self.environment.currentPlayer.ai or self.showComputer:
            if receivedCards > 0:
                print('You received {} cards').format(receivedCards)
            else:
                print('GO FISH')

    def printWinners(self):
        for player in self.environment.winners:
            print(player.name + ' ', end='')
        print('won the game!')