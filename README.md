# CSC495 PLM - GROUP O
Members:
Stewart,Grady
Su,Hang
Suh,Amy

This project allows up to four users to play Bartok or Go Fish.

# How to Run
To play, run GameRunner.py must run with the applicable arguments.
If users desire to play Go Fish, GameRunner.py should be run with the "-g GoFish" argument.
If users desire to play Bartok, GameRunner.py should be run with the "-g Bartok" argument.
Use the -p argument to indicate how many people are playing the game. For example, if there are 3 players, add "-p 3" as an argument.
If players want to add an AI player to the game, similar to adding human players, use the -c argument to indicate how many AI players to add to the game.

For example, if Go Fish is to be played with 2 human players and 2 AI players, the program should be run as "python GameRunner.py -g GoFish -p 2 -c 2".
