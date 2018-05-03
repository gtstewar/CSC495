class Environment():
    def __init__(self, players, deck, currentPlayer):
        self.players = players
        self.deck = deck
        self.winners = []
        self.currentPlayer = currentPlayer
        self.previousPlayer = None