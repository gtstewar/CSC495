from DeckConfig import Pile
from Rules import *
import sys


class Player(Pile):
    def __init__(self, name, self_func):
        super(Player, self).__init__([])
        self.name = name
        self.func = self_func

    @classmethod
    def play(cls, *info):
        pass


# We need to use monad to pass information and state with result
# Since Most Monad are not implemented, i use List as monad
# Since List itself can be considered as a monad

class BartokPlayer(Player):
    def play(self, *info):
        if len(info) != 1:
            raise SyntaxError
        print "<" + self.name + ">" + " met this card: "
        print_formatted(show % info[0][0])
        toss, self.cards = self.func(L[self.cards], info[0])
        self.cards = [i for i in self.cards]
        if len(toss) != 0:
            print "<" + self.name + ">" + " tossed this:"
            print_formatted(hand_show % toss)
        else:
            print "<" + self.name + ">" + " tossed nothing"
        return toss


# print type_of(L[[CD(Diamond, Four)]])
# a = BartokPlayer("Anthony", bartok_rule_player)
# a.get(CD(Spade, Ten))
# a.get(CD(Spade, Nine))
# a.get(CD(Spade, Eight))
# a.get(CD(Diamond, King))
# a.play(L[[CD(Diamond, Four)]])
#
# a = BartokPlayer("AI Dummy", bartok_rule_ai_intelligent)
# a.get(CD(Spade, Ten))
# a.get(CD(Spade, Nine))
# a.get(CD(Spade, Eight))
# a.get(CD(Diamond, King))
# a.play(L[[CD(Spade, Four)]])

class GoFishPlayer(Pile):
    def __init__(self, is_ai, number):
        super(GoFishPlayer, self).__init__([])
        self.ai = is_ai
        self.book_num = 0
        if not self.ai:
            print 'Enter your name Player ' + str(number + 1) + ' : '
            self.name = sys.stdin.readline().strip()
        else:
            self.name = 'Computer ' + str(number + 1)

    def display_current_hand(self):
        temp_list = L[self.cards]
        list_len = len(self.cards)
        print_formatted(hand_show % temp_list)

        for i in range(list_len):
            print "  {:>2}   ".format(i),
        print ""

    def __contains__(self, item):
        for i in self.cards:
            if i == item:
                return True
        return False

    def check_by_rank(self, item):
        for i in self.cards:
            if i.i1 == item.i1:
                return True
        return False

    def give_up_all_by_rank(self, item):
        matched_card = [c for c in self.cards if c.i1 == item]
        self.cards = [c for c in self.cards if c not in matched_card]

    def check_for_book_hand(self):
        value_lb, value_hb = bounds % Two
        for i in L[value_lb, ..., value_hb]:
            counter = 0
            for c in self.cards:
                if c.i1 == i:
                    counter += 1
                    if counter == 4:
                        print "You got a book"
                        for ca in reversed(self.cards):
                            if ca.i1 == i:
                                self.cards.remove(ca)
                        self.book_num += 1
                        return True
        return False

    def computer_pick_a_card(self):
        card = None
        max_count = 0
        value_lb, value_hb = bounds % Two
        for i in L[value_lb, ..., value_hb]:
            counter = 0
            for c in self.cards:
                if c.i1 == i:
                    counter += 1
                if counter > max_count:
                    card = c
                    max_count = counter
        if card is not None:
            return card
        return self.cards[0]


# a = GoFishPlayer(True, 0)
# a.get(CD(Spade, Ten))
# a.get(CD(Diamond, King))
# a.get(CD(Spade, King))
# a.get(CD(Club, King))
# a.get(CD(Heart, King))
# print a.check_for_book_hand()
# a.display_current_hand()
# print CD(Diamond, King) in a
# print a.check_by_rank(CD(Diamond, King))
# a.give_up_all_by_rank(King)
# print CD(Diamond, King) in a
# print a.book_num
