from Game import *
from interface import *
from Deck import *
from player import *
from Environment import *
import sys

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
        # transition.actions[0]()

    def step(self):
        for t in self.transitions:
            if t.guard is not None:
                if t.guard == True:
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
# GOFISH States -------------------------------------------------

class Start(State):
    def __init__(self, name, environment, ui, model):
        super(Start, self).__init__(name, environment)
        # super(Start, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        print("Welcome to Snip Snap Snorem! We will begin the game with this card:")
        #deal cards
        self.model.setUp()
        self.ui.displayStartingCard(self.environment.currentPlayer.getCardToStart())


class Play(State):
    def __init__(self, name, environment, ui, model):
        super(Play, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #display pertinent player info
        self.ui.displayDash()
        # Block for a correct card selection
        self.ui.promptUserForCard()
        card = self.model.receiveCard()
        while card is None:
            self.ui.displayMessageToUser('Invalid Card')
            self.ui.promptUserForCard()
            card = self.model.receiveCard()
        cardToPlay = self.model.executeTurn(card, self.environment.currentPlayer)
        if self.environment.currentPlayer.isEmptyHand():
            #temp code
            print("You won!")
            sys.exit()
        self.model.switchTurns()

    def step(self):
        if len(self.environment.deck.facedown) == 0:
            return self.transitions[0].end
        else:
            return self

class End(State):
    def __init__(self, name, environment, ui, model):
        super(End, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #print winners and exit
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
        # super(GoFishGame, self).__init__(start)
        play = Play('Play', environment, ui, model=gameModel)
        end = End('End', environment, ui, model=gameModel)
        #add transitions
        start.addtransition(Transition(True, play))
        play.addtransition(Transition(lambda: environment.deck.isEmpty(), end))
        play.addtransition(Transition(True, play))
        #add states to machine
        self.states.append(start)
        self.states.append(play)
        self.states.append(end)
        self.currentstate = start
        self.run()

    def run(self):
        super(SnipSnapSnoremGame, self).run()

