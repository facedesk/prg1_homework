#problem 1

'''
Write a class that represents a Dice

Member variables:
*int sides #this represents the number of sides the dice can have

*int side_up #this represents the side that is currently up

Functions:
init function # take in sides and set member variable. set side_up to the max sides.

Roll # use a random number generator to change the value of side_up

'''

#problem 2
'''
Write a class that represents a player called Player
Member Variables:

-turn_wins
-game_wins 
-name

Functions:
init # take in name and set name. Set score to zero

Display_Status # no parameters print players name, their turn_wins, and game wins

Take_Turn # take in a list of dice and roll them all. return the sum of their face ups
'''

#Problem 3
'''
Write a class called game that represents a full game of dice
This class will have to import the previous classes

Member Variables:
list - players
int - max_score


Functions:
init # take in players list, set max score to 3

play # play the dice game using the previous objects

play_round # represe
nts one round of all players rolling and choosing the highest score

check_winner # searches through all players returning the player that won. If no one has won, return False
'''

