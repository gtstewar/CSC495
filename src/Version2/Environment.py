class Environment():
    def __init__(self, players, deck, currentPlayer):
        self.players = players
        self.deck = deck
        self.winners = None
        self.currentPlayer = currentPlayer