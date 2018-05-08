import argparse
from StateMachine import *
from interface import *
from Deck import *
from player import *
from Environment import *
import os

#parse the incoming command line arguments
def parse_arguments():
  parser = argparse.ArgumentParser(description = 'Configuration Manager for ChaseTheAce')
  parser.add_argument('-p', dest='players', type = int, default = None,
    help = 'number of human players...total players (Players + computers) cant be greater than 4')
  parser.add_argument('-c', dest='computers', metavar='AIs', type=int,
    default = 0,
    help = 'Number of Computer players...total players (Players + computers) cant be greater than 4')
  parser.add_argument('-n', dest='simulations', type = int, default = 1, help = 'How many games do you want to play')
  parser.add_argument('-s', dest='showComputerScreen', type = int, default = 1, help = 'Do you want to see the computers screens when its their turn, 1 for yes...0 for no')

  return parser.parse_args()

def main():
    args = parse_arguments()


    if args.simulations < 1:
        raise Exception('-s must be a numerical value > 0')
    if args.players + args.computers > 4 or args.players + args.computers < 2 :
        raise Exception('There cannot be more than 4 total players or less than 2')
    for i in range(args.simulations):
        players = []
        #initiate deck
        pile = deck(True)
        #initiate players
        for i in range(args.players):
            players.append(ChaseTheAcePlayer(False, i, name='Player ' + str(i)))
        for i in range(args.computers):
            players.append(ChaseTheAcePlayer(True, i + args.players, name='Computer ' + str(i)))

        #pass the above initiated objects into Environment
        env = Environment(players, pile, players[0])
        #inititate interface
        if args.showComputerScreen == 0:
            ui = Interface(False, env)
        else:
            ui = Interface(True, env)
        #create machine and let it run off into the sunset
        game = ChaseTheAceGame(env, ui)

    return 0

if __name__ == '__main__':
    main()
