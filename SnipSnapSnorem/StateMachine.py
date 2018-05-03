from Game import *
from interface import *
from Deck import *
from player import *
from Environment import *

rankCount = 0

class Transition(object):
    def __init__(self, guard, end):
        self.guard = guard
        self.end = end

class State(object):
    def __init__(self, name, environment):
        self.environment = environment
        self.name = name
        self.transitions = []

    def onEntry(self):
        pass

    def addtransition(self, transition):
        self.transitions.append(transition)

    def step(self):
        for t in self.transitions:
            if t.guard() is not None:
                if t.guard() == True:
                    return t.end

    def onEntry(self):
        pass

    def quit(self):
        return True

class Start(State): pass

class FSM(object):
    def __init__(self, start):
        self.states = []
        self.start = start
        self.currentstate = start
        self.run()

    def addState(self, state):
        self.states.append(state)

    def run(self):
        while True:
            self.currentstate.onEntry()
            self.currentstate = self.currentstate.step()
            if isinstance(self.currentstate, End) :
                self.currentstate.onEntry()
                break
# SNIPSNAPSNOREM States -------------------------------------------------

class Start(State):
    def __init__(self, name, environment, ui, model):
        super(Start, self).__init__(name, environment)
        # super(Start, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        self.ui.displayMessageToUser("Welcome to Snip Snap Snorem!")
        #deal cards
        self.model.setUp()
        # place one of first player's cards on top of discard pile
        self.model.firstCardOnDiscardPile(self.environment.currentPlayer.getCardToStart())

class Play(State):
    def __init__(self, name, environment, ui, model):
        super(Play, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        print("------------------------------------------------------")
        self.ui.displayMessageToUser(str(self.environment.currentPlayer.name) + "'s turn")
        #display pertinent player info
        self.ui.displayMessageToUser("Choose a card from your hand with the same rank as the following card by typing in the corresponding number.\nIf not, select any card in your hand.")
        cardToDisplay = []
        self.model.getFirstCardOnDiscardPile()
        cardToDisplay.append(self.ui.getCardToDisplay(self.model.getFirstCardOnDiscardPile()))
        self.ui.printCards(1, 1, cardToDisplay)
        self.ui.displayDash()
        # Block for a correct card selection
        self.ui.promptUserForCard()
        card = self.model.receiveCard()
        while card is None:
            self.ui.displayMessageToUser('Invalid Card')
            self.ui.promptUserForCard()
            # reads user input for card
            card = self.model.receiveCard()
        if card == -1: #current player has nothing to play
            self.model.switchTurns()
        received = self.model.executeTurn(self.model.getFirstCardOnDiscardPile(), self.environment.currentPlayer)
        if received != -1 and received != 0:
            global rankCount
            rankCount += 1
            if rankCount == 1:
                self.ui.displayMessageToUser("SNIP!")
            elif rankCount == 2:
                self.ui.displayMessageToUser("SNAP!")
            elif(rankCount == 3):
                self.ui.displayMessageToUser("SNOREM! You will start the next round! Choose any card from your hand by typing in the corresponding number.")
                rankCount = 0 #reset count
                self.ui.displayDash()
                self.ui.promptUserForCard()
                card = self.model.receiveCard()
                while card is None:
                    self.ui.displayMessageToUser('Invalid Card')
                    self.ui.promptUserForCard()
                    # reads user input for card
                    card = self.model.receiveCard()
                self.model.executeTurn(card, self.environment.currentPlayer)
        self.model.switchTurns()

class End(State):
    def __init__(self, name, environment, ui, model):
        super(End, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #print winner and exit
        self.model.findWinners()
        self.ui.printWinners()
        return True

#SnipSnapSnorem Machine ----------------------------------------------------------
class SnipSnapSnoremGame(FSM):
    def __init__(self, environment, ui):
        self.states = []
        #initate the model for the game
        gameModel = SnipSnapSnorem(environment)
        #create the states
        start = Start('Start', environment, ui, model=gameModel)
        play = Play('Play', environment, ui, model=gameModel)
        end = End('End', environment, ui, model=gameModel)
        #add transitions
        start.addtransition(Transition(lambda: True, play))
        play.addtransition(Transition(lambda: environment.currentPlayer.isEmptyHand(), end))
        play.addtransition(Transition(lambda: True, play))
        #add states to machine
        self.states.append(start)
        self.states.append(play)
        self.states.append(end)
        self.currentstate = start
        self.run()

    def run(self):
        super(SnipSnapSnoremGame, self).run()