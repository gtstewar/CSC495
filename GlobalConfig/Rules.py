from CardConfig import *
from random import randint


@TS(C / [Card] >> [Card] >> ([Card], [Card]))
def bartok_rule_player(card_in_hand, card_face_ups):
    card_face_up = card_face_ups[0]
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


@TS(C / [Card] >> [Card] >> ([Card], [Card]))
def bartok_rule_ai_random(card_in_hand, card_face_ups):
    card_face_up = card_face_ups[0]
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


@TS(C / [Card] >> [Card] >> ([Card], [Card]))
def bartok_rule_ai_intelligent(card_in_hand, card_face_ups):
    card_face_up = card_face_ups[0]
    temp = [i for i in card_in_hand
            if card_face_up.i0 == i.i0 or
            card_face_up.i1 == i.i1]
    if len(temp) == 0:
        print "Nothing to toss"
        return L[[]], L[[i for i in card_in_hand]]
    else:
        unit_count_face = 0
        for i in card_face_ups:
            if i.i0 == card_face_up.i0:
                unit_count_face += 1
        unit_count_hand = 0
        for i in card_in_hand:
            if i.i0 == card_face_up.i0:
                unit_count_hand += 1
        value_count_face = 0
        for i in card_face_ups:
            if i.i1 == card_face_up.i1:
                value_count_face += 1
        value_count_hand = 0
        for i in card_in_hand:
            if i.i1 == card_face_up.i1:
                value_count_hand += 1
        unit_rate = (unit_count_hand + unit_count_face) / 13.0
        value_rate = (value_count_hand + value_count_face) / 4.0
        if value_count_hand == 0 and unit_count_hand != 0:
            temp = [i for i in temp if i.i0 == card_face_up.i0]
        elif value_count_hand != 0 and unit_count_hand == 0:
            temp = [i for i in temp if i.i1 == card_face_up.i1]
        elif value_count_hand != 0 and unit_count_hand != 0:
            if unit_rate > value_rate:
                temp = [i for i in temp if i.i1 == card_face_up.i1]
            else:
                temp = [i for i in temp if i.i0 == card_face_up.i0]
        respond = randint(0, len(temp) - 1)
        card_in_hand = [i for i in card_in_hand if i != temp[respond]]
        return L[[temp[respond]]], L[card_in_hand]
