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

# Bartok Rules
...as described at https://en.wikipedia.org/wiki/Bartok_(card_game)
### How to Win:
The goal is to be the first player to empty one’s hand of all cards.
### Rank of Cards:
The cards are all of the standard cards (jokers not included)
The suits and numbers matter as they determine what cards can be played, but there is no card  hierarchy in this game
### How to Deal:
Cards are shuffled and placed in a stack in the center of the circle
Players agree to play with either 5 or 7 cards
Cards are dealt in the standard manner by a dealer chosen by the group
### How to Play:
One card is flipped of the deck, creating a separate pile with the card faceup
Play begins left of the dealer in a clockwise manner
The player whose turn it is can do one of three things, play a card of matching number to the card on top of the faceup discard pile, play a card of matching suit to the card on the faceup discard pile, or draws a new card from the facedown deck
If a player has one card left, s/he must say “Bartok” or pick up one penalty card.
Play continues in this manner until a player has no cards left -> this player is the winner
The winner of the round gets to add a rule for the next round
These rules must be in the form if - condition, then - action
Cannot specifically target or only apply to one player
Commonly include things such as granting special powers to certain card(such as playing a 7 skips the next person) or changing the course of play
These rules may contradict other rules already enacted as the new rule has precedence over older rules
These rules compound on each other until play is ended for the session
### Strategy & How to Win:
Luck -- Drawing a card from the draw pile that has the same number or suit to the card on top of the discard pile when your turn comes around. Drawing cards of the same suit can also contribute to success
Attentiveness -- Players can prevent others from winning by being aware of how many cards others have at all times. By saying “Bartok” before the player who is left with one card, a player can prevent them from winning.
### How to Bluff:
There is no real opportunity to bluff in this game
### Turn Structure:
Turn structure remains constant for the first round but can be changed from round to round and even inside a round according to new rules added by the winner of each round

