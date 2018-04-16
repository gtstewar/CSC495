from CardConfig import *
from random import shuffle, seed
from Pyskell import *


@TS(C / ["a"] >> ["a"])
def h_shuffle(h_l):
    temp_l = [_i for _i in h_l]
    shuffle(temp_l)
    return L[temp_l]


@TS(C / int >> [Card])
def init_face_down(sd):
    seed(sd)
    unit_lb, unit_hb = bounds % Diamond
    value_lb, value_hb = bounds % Two
    init_list = [CD(_i, j) for _i in L[unit_lb, ..., unit_hb]
                 for j in L[value_lb, ..., value_hb]]
    shuffle(init_list)
    return L[init_list]
