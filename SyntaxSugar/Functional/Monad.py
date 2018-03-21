from UtilBasic import BaseObject
from SyntaxSugar.Functional.Exception import *
from UtilBasic.BaseSettings import ABT


"""
Constraint!
SequentialMonad is FoldAble, it is strong typed.
"""


def identity(x):
    return x


class Monad(BaseObject):
    """Providing the basic interface for a monad"""
    def __init__(self, content):
        self.content = content

    def f_map_with(self, func):
        """(a -> b) -> f a -> f b"""
        self.content = func(self.content)
        return self


class SequentialMonad(Monad):
    """Some sequential Monad from Haskell Util"""
    def __init__(self, content):
        """Check if content sequential in initialize"""
        Monad.__init__(self, content)
        if not self.__is__sequential__():
            raise NotSequentialException

    def __is__sequential__(self):
        return any([isinstance(self.content, ABT),
                    isinstance(self.content, list)])

    def f_map_with(self, func):
        """(a -> b) -> f a -> f b"""
        self.content = type(self.content)(map(func, self.content))
        return self

    def filter_with(self, func):
        """(a -> Bool) -> f a -> f a"""
        self.content = type(self.content)(filter(func, self.content))

    def fold_l(self, func, init):
        """from haskell foldl, Foldable t => (b -> a -> b) -> b -> t a -> b"""
        pass

    def fold_r(self, func, init):
        """from haskell foldr, Foldable t => (a -> b -> b) -> b -> t a -> b"""
        pass

    def fold_l1(self, func):
        """from haskell foldl1, Foldable t => (a -> a -> a) -> t a -> a"""
        pass

    def fold_r1(self, func):
        """from haskell foldr1, Foldable t => (a -> a -> a) -> t a -> a"""
        pass


class MaybeMonad(Monad):
    """Maybe Monad from Monad base class"""
    def __init__(self, content):
        Monad.__init__(self, content)

    def f_map_with(self, func):
        if self.is_anything():
            self.content = func(self.content)
        return self

    def is_anything(self):
        return self.content is not None

    def just(self):
        pass

    def nothing(self):
        pass


class EitherMonad(Monad):
    pass
