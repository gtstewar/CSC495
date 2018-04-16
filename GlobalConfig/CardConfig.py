from Pyskell.Language.Syntax.ADTs import *
from Pyskell.Language.TypeClasses import *
from Pyskell.Language.Syntax.Pattern import *
from Pyskell.Language.EnumList import Enum
from Pyskell.Data.String import *


(Unit,
 Spade, Heart,
 Diamond, Club) = data.Unit == d.Spade \
                             | d.Heart \
                             | d.Diamond \
                             | d.Club \
                             & deriving(Eq, Ord, Bounded, Enum)

Instance(Show, Unit).where(
    show=lambda _x: ~(CaseOf(_x) | pb(Spade) >> '2660'
                                 | pb(Heart) >> '2665'
                                 | pb(Diamond) >> '2666'
                                 | pb(Club) >> '2663'))


@TS(C / Unit >> unicode)
def show_unit(var):
    if not isinstance(var, Unit):
        raise TypeError("Error in show unit")
    return unichr(int(show % var, 16))


(Value,
 Three, Four, Five, Six,
 Seven, Eight, Nine, Ten,
 Jack, Queen, King, Ace,
 Two) = data.Value == d.Three | d.Four | d.Five | d.Six \
                    | d.Seven | d.Eight | d.Nine | d.Ten \
                    | d.Jack | d.Queen | d.King | d.Ace \
                    | d.Two & deriving(Eq, Ord, Enum, Bounded)

Instance(Show, Value).where(
    show=lambda _x: ~(CaseOf(_x) | pb(Three) >> '3'
                                 | pb(Four) >> '4'
                                 | pb(Five) >> '5'
                                 | pb(Six) >> '6'
                                 | pb(Seven) >> '7'
                                 | pb(Eight) >> '8'
                                 | pb(Nine) >> '9'
                                 | pb(Ten) >> '10'
                                 | pb(Jack) >> 'J'
                                 | pb(Queen) >> 'Q'
                                 | pb(King) >> 'K'
                                 | pb(Ace) >> 'A'
                                 | pb(Two) >> '2'))


# Convention, first unit, then value


(Card, CD) = data.Card == d.C("a", "b") & deriving(Eq)


Instance(Show, Card).where(
    show=lambda _x:
    ~(CaseOf(_x) | pb(CD(pb.x, pb.y)) >>
      "+-----+\n" +
      "|{:<2}   |\n".format(show % va.y) +
      "|  {}  |\n".format("\\u" + show % va.x) +
      "|   {:>2}|\n".format(show % va.y) +
      "+-----+"))


def print_formatted(var):
    print var.encode('ascii').decode('unicode_escape')


@TS(C / [Card] >> str)
def hand_show(cards):
    temp = []
    for i in cards:
        temp.append(lines * show % i)
    card_len = len(temp[0])
    res = ""
    for i in range(card_len):
        for j in temp:
            res += j[i]
        res += "\n"
    return res
