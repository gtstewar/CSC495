from Game import *
from interface import *
from Deck import *
from player import *
from Environment import *

count = 0

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
# CHASETHEACE States -------------------------------------------------

class Start(State):
    def __init__(self, name, environment, ui, model):
        super(Start, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        self.ui.displayMessageToUser("Welcome to Chase The Ace!")
        #deal cards (each player gets a single card)
        self.model.setUp()

class Play(State):
    def __init__(self, name, environment, ui, model):
        super(Play, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        print("------------------------------------------------------")
        self.ui.displayMessageToUser(str(self.environment.currentPlayer.name) + "'s turn")
        self.ui.displayMessageToUser("The goal of the game is to have the Ace card or a card that is closest in rank to Ace, where 2 is the lowest and Ace is the highest.")
        self.ui.displayMessageToUser("If you would like to keep your card, type 'stand'. If you would like to swap cards with the next player, type 'change'.")
        self.ui.displayDash()
        # Block for a correct card selection
        self.ui.promptUserForChoice()
        choice = self.model.receiveChoice()
        while choice != "change" and choice != "stand":
            self.ui.displayMessageToUser('Invalid Option')
            self.ui.promptUserForChoice()
            choice = self.model.receiveChoice()
        received = self.model.executeTurn(choice, self.environment.nextPlayer)
        self.ui.displayMessageToUser("You are ending this turn with")
        self.ui.displayCurrentPlayersInfo()
        self.model.switchTurns()
        global count
        count += 1
        if count % (len(self.environment.players)) == 0:
            self.ui.displayMessageToUser("This round's winner is " + self.model.findRoundWinner().name + "!")
class End(State):
    def __init__(self, name, environment, ui, model):
        super(End, self).__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #print winner and exit
        self.model.findOverallWinner()
        return True

#ChaseTheAce Machine ----------------------------------------------------------
class ChaseTheAceGame(FSM):
    def __init__(self, environment, ui):
        self.states = []
        #initate the model for the game
        gameModel = ChaseTheAce(environment)
        #create the states
        start = Start('Start', environment, ui, model=gameModel)
        play = Play('Play', environment, ui, model=gameModel)
        end = End('End', environment, ui, model=gameModel)
        #add transitions
        global count
        start.addtransition(Transition(lambda: True, play))
        play.addtransition(Transition(lambda: count == pow(len(environment.players), 2), end))
        play.addtransition(Transition(lambda: count % (len(environment.players)) == 0, start))
        play.addtransition(Transition(lambda: True, play))
        #add states to machine
        self.states.append(start)
        self.states.append(play)
        self.states.append(end)
        self.currentstate = start
        self.run()

    def run(self):
        super(ChaseTheAceGame, self).run()