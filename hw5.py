'''
Create a simple dice roll game. This game should use a standard 6 sided die. 
Start by asking two players to enter their names. These names should be used as entries in the scoring dictionaries mentioned at the bottom.

Each player takes alternating turns rolling the die. First ask the player(by name) to roll the die, then the player 
presses enter to roll. Then announce that it is the second players turn and ask that player to roll the die. After both players
have rolled the die, then the roll of the two players is the winner. Announce the players name who won that round and update that
players score.  When three rounds have concluded, Announce the player that has won the game so far ask the both players if they would like to play again with 1 being yes, 
and 2 being no. If both players would like to continue playing, then play best 3 of 5 rounds, and announce the player that has won the game so far.
Continue increasing the number of rounds by odd all odd numbers until the players have decided to conclude the game. 

Scoring entries:
You must use a dictionary to store the player turn scores and the player round scores.

Extra Credit 5%: at the end of each game, write to a csv file named scores.csv. This will keeping track of each player name and how many games they have won,
And display the top 10 names who have won the most. 

The format should be read as:
Stephen,4
Alfonzo,3
Shirley,3
Jeeves,0

'''
