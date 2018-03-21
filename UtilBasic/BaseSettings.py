from BaseObject import *


class ABT(BaseObject):
    """Abstract Binding Tree, Check PFPL Chapter 1"""
    def __init__(self, **dic_args):
        self.__dict__.update(dic_args)


"""
example = ABT(group_o=ABT(Grady="Great coder",
                          Amy="Great help",
                          Anthony="Some humble nomad monad"),
              instructor=ABT(Timm="The most handsome sage in the world"),
              course="CSC495 NCSU 2018 Spring")
"""
