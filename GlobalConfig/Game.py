from MagicCircle import *


class GameFSM(object):
    def __init__(self, env):
        if not isinstance(env, MCEnv):
            raise TypeError
        self.env = env

    def run(self):
        pass
