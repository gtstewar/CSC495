class Environment():
    def __init__(self, players, deck, currentPlayer):
        self.players = players
        self.deck = deck
        self.winners = []
        self.currentPlayer = currentPlayer
        # self.previousPlayer = None
        index = players.index(currentPlayer)
        self.nextPlayer = players[index + 1]
        self.nextNextPlayer = players[index + 2]