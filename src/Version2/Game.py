from src.GoFish import Deck
from src.GoFish.player import *
import random

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Game():
    def __init__(self, environment):
        pass

class GoFish(Game):

    def play(self):
        print('here')

    def findWinners(self, environment, ui):
        print('Winners')

    def getPlayerChoicesAndPrint(self, player):
        choicesDic = {}

