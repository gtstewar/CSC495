import os
import time


class ExportToCmd(object):
    def __init__(self):
        pass

    @staticmethod
    def clear():
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')


screen_refresh = ExportToCmd()
