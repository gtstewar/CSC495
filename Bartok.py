from GlobalConfig import *


class BartokEnv(MCEnv):
    def start_env(self):
        for i in self.players:
            if not isinstance(i, Player):
                raise TypeError
        for _ in range(5):
            for j in self.players:
                j.get(self.face_down.extract())
        self.face_up.get(self.face_down.extract())


class BartokMachine(GameFSM):
    def run(self):
        self.env.start_env()
        while True:
            curr_p = self.env.players[self.env.current_player]
            print "\n"
            for i in self.env.players:
                print "<" + i.name + ">: " + str(i.contain_num())
            print "\n"
            res = curr_p.play(self.env.face_up.cards)
            if len(res) == 0:
                curr_p.get(self.env.face_down.extract())
            else:
                self.env.face_up.get(res[0])
            if self.env.check_is_win(curr_p):
                print "<" + curr_p.name + "> " + " wins"
                break
            else:
                self.env.next_player()
                screen_refresh.clear()


a = BartokMachine(BartokEnv([BartokPlayer("tired", bartok_rule_player),
                            BartokPlayer("exhausted", bartok_rule_ai_random)],
                            lambda _x: _x.empty()))

a.run()
