from src.Version2.Game import *
from src.Version2.Environment import *
from src.Version2.player import *
from src.Version2.interface import *
from src.Version2.Deck import *

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
                if (t.guard is True):
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
            if self.currentstate.name == 'End' :
                break

class Start(State):
    def __init__(self, name, environment, ui, model):
        self.environment = environment
        self.name = name
        self.transitions = []
        self.ui = ui
        self.model = model

    def onEntry(self):
       self.model.setUp()

class Play(State):
    def __init__(self, name, environment, ui, model):
        self.environment = environment
        self.name = name
        self.transitions = []
        self.ui = ui
        self.model = model

    def onEntry(self):
        self.ui.displayDash()
        self.ui.promptUserForCard()
        card = self.model.receiveCard()
        while card is None:
            self.ui.displayMessageToUser('Invalid Card')
            self.ui.promptUserForCard()
            card = self.model.receiveCard()
        self.ui.promptUserForPlayerToAsk()
        playerToAsk = self.model.receivePlayer()
        while playerToAsk is None:
            self.ui.displayMessageToUser('Invalid Player')
            self.ui.promptUserForPlayerToAsk()
            playerToAsk =self.model.receivePlayer()
        receivedCards = self.model.executeTurn(card, playerToAsk)
        self.ui.receivedCardsMessage(receivedCards)
        self.model.switchTurns()


class End(State):
    def __init__(self, name, environment, ui, model):
        self.environment = environment
        self.name = name
        self.transitions = []
        self.ui = ui
        self.model = model

    def onEntry(self):
        self.model.findWinners()
        self.ui.printWinners()
        return True

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
        play.addtransition(Transition(len(environment.deck.facedown) != 0, play))
        play.addtransition(Transition(len(environment.deck.facedown) == 0, end))

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
players.append(GoFishPlayer(False, 3, name='Jerry'))
players.append(GoFishPlayer(False, 4, name='Mary-Anne'))
Deck = deck(True)
env = Environment(players, Deck, players[0])
inter = Interface(True, env)
GoFishGame(env, inter)
