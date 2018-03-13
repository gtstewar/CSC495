# CSC495 PLM - GROUP O
Members:

Stewart,Grady</br>
Su,Hang</br>
Suh,Amy

This project allows up to four users to play Bartok or Go Fish.

# How to Run
To play, run GameRunner.py must run with the applicable arguments.

If users desire to play Go Fish, GameRunner.py should be run with the "-g GoFish" argument.</br>
If users desire to play Bartok, GameRunner.py should be run with the "-g Bartok" argument.</br>
Use the -p argument to indicate how many people are playing the game. For example, if there are 3 players, add "-p 3" as an argument.</br>
If players want to add an AI player to the game, similar to adding human players, use the -c argument to indicate how many AI players to add to the game.</br>
For example, if Go Fish is to be played with 2 human players and 2 AI players, the program should be run as "python GameRunner.py -g GoFish -p 2 -c 2".

# Bartok Rules
...as described at https://en.wikipedia.org/wiki/Bartok_(card_game)
### How to Win:
The goal is to be the first player to empty one’s hand of all cards.
### Rank of Cards:
The cards are all of the standard cards (jokers not included)</br>
The suits and numbers matter as they determine what cards can be played, but there is no card  hierarchy in this game
### How to Deal:
Cards are shuffled and placed in a stack in the center of the circle</br>
Players agree to play with either 5 or 7 cards</br>
Cards are dealt in the standard manner by a dealer chosen by the group
### How to Play:
One card is flipped of the deck, creating a separate pile with the card faceup</br>
Play begins left of the dealer in a clockwise manner</br>
The player whose turn it is can do one of three things, play a card of matching number to the card on top of the faceup discard pile, play a card of matching suit to the card on the faceup discard pile, or draws a new card from the facedown deck</br>
If a player has one card left, s/he must say “Bartok” or pick up one penalty card.</br>
Play continues in this manner until a player has no cards left -> this player is the winner!</br>
The winner of the round gets to add a rule for the next round</br>
These rules must be in the form if - condition, then - action</br>
Cannot specifically target or only apply to one player</br>
Commonly include things such as granting special powers to certain card(such as playing a 7 skips the next person) or changing the course of play</br>
These rules may contradict other rules already enacted as the new rule has precedence over older rules</br>
These rules compound on each other until play is ended for the session
### Strategy & How to Win:
Luck -- Drawing a card from the draw pile that has the same number or suit to the card on top of the discard pile when your turn comes around. Drawing cards of the same suit can also contribute to success</br>
Attentiveness -- Players can prevent others from winning by being aware of how many cards others have at all times. By saying “Bartok” before the player who is left with one card, a player can prevent them from winning.
### How to Bluff:
There is no real opportunity to bluff in this game
### Turn Structure:
Turn structure remains constant for the first round but can be changed from round to round and even inside a round according to new rules added by the winner of each round

# Go Fish
### How to Win:
The goal is to have the most books of cards.</br>
(A book is the set of four cards of the same value, such as a 3 of hearts, a 3 of spades, a 3 of clubs, and a 3 of diamonds.)
### Rank of Cards:
The cards from from 2 (low) to Ace (high).</br>
Only the card numbers are relevant; suits can be ignored.
### How to Deal:
Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards.</br>
For games with three players or more, the dealer deals five cards to each player. For games with two players, each player gets seven cards. The cards are dealt clockwise starting with the dealer.</br>
The remaining cards are placed face down to form a stock pile.
### How to Play:
Each player is dealt five cards. The stack of remaining cards are placed face-down in the center as the draw pile.</br>
Before beginning the game, each player inspects their hand and removes all "books" of cards, meaning 4 cards of the same value. (e.g. If a player is dealt a 3, 7, 7, 7, 7 they would remove all four 7's, and they would be left with the 3 card)</br>
Moving clockwise, players take turns asking another player for a given rank of card (“fishing”). This player must have at least one card of the rank s/he has asked for in their hand.</br>
If the other player has the needed card(s), they must pass all cards of that rank over to the asking player.</br>
If not, the player must “go fish” by taking one new card from the top of the draw pile.</br>
If a player runs out of cards during the game, they must pick up a card from the stock pile and play their usual turn by asking another player for cards of that value.
The play continues until the stock pile is depleted.
### Strategy & How to Win:
Luck -- Drawing a card from the draw pile that has the same rank as one of the cards in your hand.</br>
Memory -- Keeping track of which cards other players have by remember their requests on their turn.
### How to Bluff:
There is no real opportunity to bluff in this game
### Turn Structure:
Turn structure remains constant the whole game

