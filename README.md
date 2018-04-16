# CSC495 PLM - GROUP O
Members:

Stewart,Grady</br>
Su,Hang</br>
Suh,Amy

This project allows up to four users to play Bartok or Go Fish.

# How to Run
First, clone this repository. To play, run GameRunner.py with the applicable arguments explained below.

### Bartok

run `python Bartok.py`.

### Go Fish

run `python ./GoFish/GoFishRunner.py` wit command line arguments:
-c {number of computers}
-p {number of human players}
-n {number of games}
-s {Show computer moves} - 0 to not show the computers dash, 1 to show computers dash.

-c and -p are required but -n and -s are not and have default values of 1 and 1 respectively

Example: python ./GoFish/GoFishRunner.py -c 2 -p 2 -n 2 -s 0 

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

## Usage and Video:

```python
from Game_2 import Bartok

if __name__ == '__main__':
    a = Bartok(["a", "b", "c", "d"])
    a.run()
```

Module `Game_2` is contains only `Bartok` class.

Passing a list of user name (human), the length should be less or equal to 4.

Then start the class method `run()`, we can start the game.

Ehhhhhhh..... Read the code for the rest of instruction... OR SO TO SAY RTFM...LOL...

No kidding now... If you want to choose the card, just choose the index number for the card.
The computer will take care of the rest.

Enjoy :-)

[Example Video Link](https://drive.google.com/file/d/12c5LgeVuH6CAJKypfPC83gH4dDMLdOU0/view?usp=sharing)

> BTW, if you are not sure about what's happening, you can pass a empty list into `Bartok` class.
> The algorithm of bartok will take care of itself, then finish all the stuff till some AI win.
> Sounds like some AlphaGo stuff lol.

# Go Fish
[Example Video Link](https://drive.google.com/open?id=1XKh0GJZnvD7f7Z5LH80eWrEb415avzOz)
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

