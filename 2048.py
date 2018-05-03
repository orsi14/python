from random import *
from numpy import *

def print_matrix():
	
	for a in range(game_size):
		print("|", end=' ')
		for b in range(game_size):
			print(matrix[a][b], "\t|", end=' ')
		print()
	print
						
				
def move(matrix, direction="left"):

	# define a bunch of values for each direction of motion
	directionLookup = {"left": [-1,1,game_size-1,1], "right": [1,game_size-2,0,-1], "up": [-1,1,game_size-1,1], "down": [1,game_size-2,0,-1]}
	
	if direction is "up" or direction is "down":
		matrix = matrix.transpose()
		print(matrix)	
	
	dirCol = directionLookup[direction][0]
	startCol = directionLookup[direction][1]
	endCol = directionLookup[direction][2]
	stepDir = directionLookup[direction][3]
	
	# for each row, start from the second from the left and move it as far left as possible
	# then move to the next cell and do the same
	hasMoved = False
	
	#go through every row (arow will be 0,1,2,3)
	for arow in range(game_size):
		#within each row, go through each column (1,2,3) or (2,1,0), either left to right or right to left
		for acol in range(startCol,endCol+stepDir,stepDir):
				
			# the first thing we're going to do is combine any cells that should be combined (same value as the cell next to it)
			# constraint is that only 2 cells can be merged together, no double merging or multi-step merging
			
			#if the box is not empty - if it's empty we dont care about moving anything in it
			if matrix[arow][acol] is not " ":
				# in this block, we've found a number.  
				# start looking in the previous cell, which has index of checkCol
				checkCol = acol+dirCol
				
				print("Found a thing to move. It's value is '",matrix[arow][acol],"'",)
				print("Box of interest at (", arow, ",",acol, ") is ", matrix[arow][acol])
				print("To its", direction, "has a value of ", matrix[arow][checkCol])
				
				# keep moving the cell until we hit the end of find a non-empty cell
				while checkCol >= 0 and checkCol < game_size and matrix[arow][checkCol] == "":
					
					# if we move the cell, register that we moved it so we know to add a new box
					hasMoved = True
					
					print("Empty box at (", arow, ",",checkCol,") is ", matrix[arow][checkCol])
					print("Putting value ", matrix[arow][checkCol+stepDir], "into it")
										
					matrix[arow][checkCol] = matrix[arow][checkCol+stepDir]
					matrix[arow][checkCol+stepDir] = ""
					checkCol -= stepDir
					print_matrix()
	
	for arow in range(game_size):
		for b in range(startCol+dirCol,endCol,stepDir):
			# if the cell to the right is the same, squish em together
			# and then move all other cells one to the left
			if matrix[arow][b] == matrix[arow][b+stepDir] and matrix[arow][b] is not "":
				
				hasMoved = True
				matrix[arow][b] *= 2
				matrix[arow][b+stepDir] = ""
				moveCol = b+stepDir
				while moveCol < game_size-stepDir and moveCol > 0:
					matrix[arow][moveCol] = matrix[arow][moveCol+stepDir]
					matrix[arow][moveCol+stepDir] = ""
					moveCol += stepDir
	
	if direction is "up" or direction is "down":
		matrix = matrix.transpose()
	
	return hasMoved
	
	
def add_block():
	# pick a random block value
	value = (randrange(2)+1)*2
	
	foundEmpty = False
	# pick a random coordinate and see if it is empty
	while not foundEmpty: 
		newRow = randrange(game_size)
		newCol = randrange(game_size)
		if matrix[newRow][newCol] == "":
			foundEmpty = True
			matrix[newRow][newCol] = value
		
# Define constants
# row and col define how many rows and columns are in the matrix
game_size = 4

matrix = [["" for a in range(game_size)] for b in range(game_size)]
matrix = asarray(matrix)

# Format of matrix is:
# matrix[row id][col id]
# where 0,0 is the top left

add_block()

while True:
	print_matrix()
	userInput = input("Enter a direction (a=left, s=down, d=right, w=up, q=quit): ")
	if userInput is "q": break
	if userInput is "a": 
		if move(matrix, "left"):
			add_block()
	if userInput is "s": 
		if move(matrix, "down"):
			add_block()
	if userInput is "d": 
		if move(matrix, "right"):
			add_block()
	if userInput is "w": 
		if move(matrix, "up"):
			add_block()

