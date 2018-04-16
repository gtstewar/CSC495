from src.Version2.Game import *
from src.Version2.Environment import *
from src.Version2.player import *
from src.Version2.interface import *
from src.Version2.Deck import *

class Transition():
    def __init__(self, guard, end):
        self.guard = guard
        self.end = end
        self.actions = []

    def addactions(self, f):
        self.actions.append(f)

class State():
    def __init__(self, name, environment, onEntry=None):
        if onEntry is not None: onEntry()
        self.environment = environment
        self.name = name
        self.transitions = []

    def addtransition(self, transition):
        self.transitions.append(transition)
        # transition.actions[0]()

    def step(self):
        for t in self.transitions:
            if t.guard is not None:
                if (t.guard is True):
                    for action in t.actions:
                        action(self.environment)
                    return t.end

    def onEntry(self):
        pass

    def quit(self):
        return True

class Start(State): pass


class End(State):
    def quit(self):
        return True

class FSM():
    def __init__(self, start):
        self.states = []
        self.start = start
        self.currentstate = start
        self.run()

    def addState(self, state):
        self.states.append(state)

    def run(self):
        while True:
            self.currentstate = self.currentstate.step()
            if self.currentstate.name == 'End' :
                break

class GoFishGame(FSM):
    def __init__(self, environment, ui):
        self.states = []
        gameModel = GoFish(environment)
        self.addState(State('Start', environment, ui.displayMessageToUser('Welcome to GoFish')))
        self.addState(State('Play', environment, gameModel.play()))
        self.addState(State('End', environment, gameModel.findWinners(environment, ui)))
        self.states[0].addtransition(Transition(True, self.states[1]))
        endTrans = Transition(len(environment.deck.facedown) == 0, self.states[2])
        endTrans.addactions(self.states[2].quit())
        self.states[1].addtransition(endTrans)
        self.currentstate = self.states[0]
        self.run()

    def run(self):
        super()

#debugging
players = []
players.append(Player(False, 1, name='Brad'))
players.append(Player(False, 2, name='Jim'))
players.append(Player(False, 3, name='Jerry'))
players.append(Player(False, 4, name='Mary-Anne'))
Deck = deck(True)
env = Environment(players, Deck, players[0])
inter = Interface(True, env)
GoFishGame(env, inter)
