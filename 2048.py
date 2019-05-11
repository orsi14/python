from random import *
from getch import *
from engine import *
import logging

		
# Define constants
# row and col define how many rows and columns are in the matrix
logging.basicConfig(filename='2048.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
game_size = 4

# Initialize game
myGame = Game(4)
myGame.add_block()

	# Format of matrix is:
	# matrix[row id,col id]
	# where 0,0 is the top left

while myGame.is_move_possible():
	# print("Here is the board:")
	print("Enter a direction (a=left, s=down, d=right, w=up, q=quit): ")
	directions = {'a':"left", 's':"down", 'd':"right", 'w':"up"}
	userInput = getch()
	if userInput is "q": break
	if userInput in ("a","s","d","w"): 
		if myGame.move(directions[userInput]):
			myGame.add_block()
			myGame.print_matrix()

print("\nGame Over....\n\n")

logging.info('Game completed: %d max, %d total', myGame.matrix.max(), myGame.matrix.sum())