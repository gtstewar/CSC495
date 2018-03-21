from UtilBasic import BaseObject


class MaybeMonad(BaseObject):
    """Python Version of Maybe Monad"""
    def __init__(self, something=None):
        self.Nothing = something is None
        self.Just = something
