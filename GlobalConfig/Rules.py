from CardConfig import *
from random import randint


@TS(C / [Card] >> Card >> ([Card], [Card]))
def bartok_rule_player(card_in_hand, card_face_up):
    print "have these cards: "
    print_formatted(hand_show % L[card_in_hand])
    temp = [i for i in card_in_hand
            if card_face_up.i0 == i.i0 or
            card_face_up.i1 == i.i1]
    if len(temp) == 0:
        print "Nothing to toss"
        return L[[]], L[[i for i in card_in_hand]]
    else:
        print "got these can toss: "
        print_formatted(hand_show % L[temp])
        message = ""
        for i in range(len(temp)):
            message += ("   " + str(i) + "   ")
        print message
        while True:
            try:
                if len(temp) > 1:
                    respond = int(input("choose from 0 to {}: "
                                        .format(len(temp) - 1)))
                else:
                    respond = int(input("it seems only one choice: "))
            except ValueError:
                continue
            if respond in range(len(temp)):
                break
        card_in_hand = [i for i in card_in_hand if i != temp[respond]]
        return L[[temp[respond]]], L[card_in_hand]


# var = bartok_rule_player(L[CD(Club, King), CD(Diamond, Eight)],
#                          CD(Spade, Seven))
# print_formatted(show % var[0][0])
# print_formatted(hand_show % var[1])


@TS(C / [Card] >> Card >> ([Card], [Card]))
def bartok_rule_ai_random(card_in_hand, card_face_up):
    temp = [i for i in card_in_hand
            if card_face_up.i0 == i.i0 or
            card_face_up.i1 == i.i1]
    if len(temp) == 0:
        print "Nothing to toss"
        return L[[]], L[[i for i in card_in_hand]]
    else:
        respond = randint(0, len(temp) - 1)
        card_in_hand = [i for i in card_in_hand if i != temp[respond]]
        return L[[temp[respond]]], L[card_in_hand]
