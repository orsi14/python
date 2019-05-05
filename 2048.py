from random import *
from numpy import *
from getch import *
import logging
import engine
	
def init():
	matrix = zeros(shape=(game_size,game_size))
	return matrix
	
# Define constants
# row and col define how many rows and columns are in the matrix
logging.basicConfig(filename='2048.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
game_size = 4
probability_of_four = 0.15


# Initialize game
matrix = init()
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