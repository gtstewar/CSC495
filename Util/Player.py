class Player:
    def __init__(self, player_name, ai_init=False):
        self.name = player_name
        self.is_ai = ai_init
        self.card_in_hand = []

    def query_for_card_existence(self, card):
        for i in self.card_in_hand:
            if i == card:
                return True
        return False

    def receive_card(self, card):
        self.card_in_hand.append(card)

    def toss_card(self, card):
        return self.card_in_hand.pop(
               self.card_in_hand.index(card))

    def identify_ai(self):
        return self.is_ai

    def is_win(self):
        return self.card_in_hand.__len__() == 0

    def __repr__(self):
        return self.name

    def show_card(self):
        print(self.name + " " + "got:")
        if self.card_in_hand.__len__() > 0:
            for index, card in enumerate(self.card_in_hand):
                print(index, "->", card)
        else:
            print("No card in hand")
