from random import *
from getch import *
from engine import *
import logging

		
# Define constants
# row and col define how many rows and columns are in the matrix
logging.basicConfig(filename='2048.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
game_size = 4

# Initialize game
matrix = init(game_size)
matrix = add_block(matrix)

	# Format of matrix is:
	# matrix[row id,col id]
	# where 0,0 is the top left

while is_move_possible(matrix):
	# print("Here is the board:")
	print("Enter a direction (a=left, s=down, d=right, w=up, q=quit): ")
	directions = {'a':"left", 's':"down", 'd':"right", 'w':"up"}
	userInput = getch()
	if userInput is "q": break
	if userInput in ("a","s","d","w"): 
		result = move(matrix, directions[userInput])
		matrix = result['matrix']
		if result['hasMoved'] == True:
			add_block(matrix)
			
logging.info('Game completed: %d max, %d total', matrix.max(), matrix.sum())