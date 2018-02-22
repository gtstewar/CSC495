from ..players.player import Player
from ..deck import Deck

class Game():
    def __init__(self, players, computers):
        self.maxplayers = 4
        if (players + computers) > self.maxplayers:
            raise Exception("There can only be " + self.maxplayers + " players")
        if (players + computers) <= 1:
            raise Exception("Must have at least 2 players")
        self.players = []
        for i in range(0, players):
            self.players.append(Player(False, i))
        for i in range(0, computers):
            self.players.append(Player(True, i))

class GoFish(Game):