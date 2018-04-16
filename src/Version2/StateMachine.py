from Game import *
from interface import *
from Deck import *
from player import *
from Environment import *

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
        super().__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #deal cards
        self.model.setUp()

class Play(State):
    def __init__(self, name, environment, ui, model):
        super().__init__(name, environment)
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
        #Block for a correct Player selection
        self.ui.promptUserForPlayerToAsk()
        playerToAsk = self.model.receivePlayer()
        while playerToAsk is None:
            self.ui.displayMessageToUser('Invalid Player')
            self.ui.promptUserForPlayerToAsk()
            playerToAsk =self.model.receivePlayer()
        receivedCards = self.model.executeTurn(card, playerToAsk)
        self.ui.receivedCardsMessage(receivedCards)
        self.environment.currentPlayer.checkForBook()
        self.model.switchTurns()

    def step(self):
        if len(self.environment.deck.facedown) == 0:
            return self.transitions[0].end
        else:
            return self

class End(State):
    def __init__(self, name, environment, ui, model):
        super().__init__(name, environment)
        self.ui = ui
        self.model = model

    def onEntry(self):
        #print winners and exit
        self.model.findWinners()
        self.ui.printWinners()
        return True

#GOFIsh Machine ----------------------------------------------------------
class GoFishGame(FSM):
    def __init__(self, environment, ui):
        self.states = []
        #initate the model for the game
        gameModel = GoFish(environment)
        #create the states
        start = Start('Start', environment, ui, model=gameModel)
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
        super().run()

#debugging
players = []
players.append(GoFishPlayer(False, 1, name='Brad'))
players.append(GoFishPlayer(False, 2, name='Jim'))
players.append(GoFishPlayer(True, 3, 'Computer 1'))
players.append(GoFishPlayer(True, 4, 'Computer 2'))
Deck = deck(True)
env = Environment(players, Deck, players[0])
inter = Interface(False, env)
GoFishGame(env, inter)
