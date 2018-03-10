from Util import *
from random import shuffle


class Bartok:
    def __init__(self, people_array):
        if list(people_array).__len__() > 4:
            raise Exception("More than 4 players")
        self.deck = Deck(True)
        self.player_list = []
        self.player_list += list(map(lambda x: Player(x), people_array))
        self.player_list += list(map(lambda x: Player("An AI Player " + str(x), True),
                                 list(range(4 - list(people_array).__len__()))))
        shuffle(self.player_list)
        for _ in range(5):
            for i in self.player_list:
                i.receive_card(self.deck.draw_card_from_top_of_deck())

    def run(self):
        while True:
            for player in self.player_list:
                if player.identify_ai():
                    # only one step to go
                    pass
                else:
                    player.show_card()
                    if is_exist_match_card(self.deck.get_top_card_of_discard_pile(),
                                           player.card_in_hand):
                        print("Please toss one card, at least one card match")
                        target_card = query_for_card(player.card_in_hand)
                        player.toss_card(target_card)
                        self.deck.face_up.append(target_card)
                    else:
                        print("Do not have any match, draw one card")
                        player.receive_card(self.deck.draw_card_from_top_of_deck())
                    player.show_card()
                if player.is_win():
                    print(str(player) + " wins.")
                    return


def query_for_card(list_of_card: list):
    print("Give me a card: ")
    while True:
        card_val = list(map(int, input().split(',')))
        if card_val.__len__() is not 2:
            continue
        target_card = Card(card_val[0], card_val[1])
        if any(map(lambda x: x == target_card, list_of_card)):
            return target_card
        else:
            continue


def bartok_match(c1: Card, c2: Card) -> bool:
    if c1.suit == c2.suit:
        return True
    elif c1.value == c2.value:
        return True
    return False


def is_exist_match_card(matcher: Card, list_of_cards: list) -> bool:
    return any(list(map(lambda x: bartok_match(matcher, x), list_of_cards)))
