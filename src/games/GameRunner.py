import argparse
from src.games.Game import *

def parse_arguments():
  parser = argparse.ArgumentParser(description = 'A GameRunner')
  parser.add_argument('-g', dest='game', metavar='GAMENAME', type=str,
    help = 'Name of game you want to play')
  parser.add_argument('-p', dest='players', type = int, default = 1,
    help = 'number of human players...total players (Players + computers) cant be greater than 4')
  parser.add_argument('-c', dest='computers', metavar='AIs', type=int,
    default = 0,
    help = 'Number of Computer players...total players (Players + computers) cant be greater than 4')
  parser.add_argument('-s', dest='simulations', type = int, default = 1, help = 'How many games do you want to play')

  return parser.parse_args()

def main():
    args = parse_arguments()

    if args.game == 'GoFish':
        if args.simulations < 1:
            raise Exception('-s must be a numerical value > 0')
        for i in range(args.simulations):
            goFish = GoFish(args.players, args.computers)
            goFish.run()

    elif args.game == 'Bartok':
        print('Bartok')
    else:
        print('Invalid -g argument...must be GoFish or Bartok')

    return 0

if __name__ == '__main__':
    main()