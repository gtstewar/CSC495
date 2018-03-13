from Util import *
from random import shuffle, choice
import re


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
        self.deck.face_up.append(self.deck.face_down.pop())

    def run(self):
        while True:
            for player in self.player_list:
                print("+-----------------------------------+")
                print("Card for Match is: "
                      + str(self.deck.get_top_card_of_discard_pile()))
                if player.identify_ai():
                    if is_exist_match_card(self.deck.get_top_card_of_discard_pile(),
                                           player.card_in_hand):
                        print(str(player) + " tosses one card: ")
                        candidates = list(filter(
                            lambda x: bartok_match(
                                self.deck.get_top_card_of_discard_pile(), x),
                            player.card_in_hand))
                        target_card = choice(candidates)
                        player.toss_card(target_card)
                        print(target_card)
                        self.deck.face_up.append(target_card)
                    else:
                        print(str(player) + " receives one card.")
                        player.receive_card(
                            self.deck.draw_card_from_top_of_deck(left_one=True))
                    print("+-----------------------------------+\n")
                else:
                    player.show_card()
                    if is_exist_match_card(self.deck.get_top_card_of_discard_pile(),
                                           player.card_in_hand):
                        print("Please toss one card, at least one card match")
                        target_card =\
                            query_for_card(player.card_in_hand,
                                           self.deck.get_top_card_of_discard_pile())
                        player.toss_card(target_card)
                        self.deck.face_up.append(target_card)
                    else:
                        print("Do not have any match, draw one card")
                        player.receive_card(
                            self.deck.draw_card_from_top_of_deck(left_one=True))
                    player.show_card()
                    print("+-----------------------------------+\n")
                if player.is_win():
                    print(str(player) + " wins.")
                    return


def query_for_card(list_of_card: list, matcher: Card):
    print("Give me a card: ")
    while True:
        while True:
            try:
                card_val = int(input())
                target_card = list_of_card[card_val]
            except Exception:
                print("INPUT FORMAT ERROR, RE-INPUT")
                continue
            break
        if bartok_match(list_of_card[card_val], matcher):
            return target_card
        else:
            print("ERROR IN CHOOSING THE CARD, DO NOT MATCH, RE-CHOOSE")
            continue


def bartok_match(c1: Card, c2: Card) -> bool:
    if c1.suit == c2.suit:
        return True
    elif c1.value == c2.value:
        return True
    return False


def is_exist_match_card(matcher: Card, list_of_cards: list) -> bool:
    return any(list(map(lambda x: bartok_match(matcher, x), list_of_cards)))
