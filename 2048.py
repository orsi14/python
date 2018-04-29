from random import *
from numpy import *

def print_matrix():
	
	for a in range(game_size):
		print("|", end=' ')
		for b in range(game_size):
			print(matrix[a][b], "\t|", end=' ')
		print()
	print

def move(direction="left"):
	# TO-DO: transpose function is throwing an error - not sure why - might be namespace related.
	# this function was working for left and right, but not up and down
	# for up and down, i added a transpose function so that it could use the same code as left/right
	# the direction lookup probably needs to be reviewed as it has too many options - it should be simpler by using the transpose to deal with up/down
	
	# define a bunch of values for each direction of motion
	directionLookup = {"left": [0,-1,0,1,0,game_size-1,1], "right": [0,1,0,game_size-2,0,0,-1], "up": [0,-1,0,1,0,game_size-1,1], "down": [0,1,0,game_size-2,0,0,-1]}
	
	if direction is "up" or direction is "down":
		print(matrix)
		matrix = transpose(matrix)
		
	
	dirRow = directionLookup[direction][0]
	dirCol = directionLookup[direction][1]
	startRow = directionLookup[direction][2]
	startCol = directionLookup[direction][3]
	endRow = directionLookup[direction][4]
	endCol = directionLookup[direction][5]
	stepDir = directionLookup[direction][6]
	
	# for each row, start from the second from the left and move it as far left as possible
	# then move to the next cell and do the same
	hasMoved = False
	
	for a in range(game_size):
		for b in range(startCol,endCol+stepDir,stepDir):
			if matrix[a][b] is not "":
				checkCol = b+dirCol
				
				#print "Found a thing to move.",
				#print "Box of interest at (", a, ",",b, ") is ", matrix[a][b] 
				#print "To its left has a value of ", matrix[a][checkCol]
				
				while checkCol >= 0 and checkCol < game_size and matrix[a][checkCol] == "":
					hasMoved = True
					#print "Empty box at (", a, ",",checkCol,") is ", matrix[a][checkCol]
					#print "Putting value ", matrix[a][checkCol+1], "into it"
					matrix[a][checkCol] = matrix[a][checkCol+stepDir]
					matrix[a][checkCol+stepDir] = ""
					checkCol -= stepDir
					#print_matrix()
	
	for a in range(game_size):
		for b in range(startCol+dirCol,endCol,stepDir):
			# if the cell to the right is the same, squish em together
			# and then move all other cells one to the left
			if matrix[a][b] == matrix[a][b+stepDir] and matrix[a][b] is not "":
				
				hasMoved = True
				matrix[a][b] *= 2
				matrix[a][b+stepDir] = ""
				moveCol = b+stepDir
				while moveCol < game_size-stepDir and moveCol > 0:
					matrix[a][moveCol] = matrix[a][moveCol+stepDir]
					matrix[a][moveCol+stepDir] = ""
					moveCol += stepDir
	
	#if direction is "up" or direction is "down":
		#matrix = matrix.transpose((1,0))
	
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
asarray(matrix)


# Format of matrix is:
# matrix[row id][col id]
# where 0,0 is the top left

add_block()

while True:
	print_matrix()
	userInput = input("Enter a direction (a=left, s=down, d=right, w=up, q=quit): ")
	if userInput is "q": break
	if userInput is "a": 
		if move("left"):
			add_block()
	if userInput is "s": 
		if move("down"):
			add_block()
	if userInput is "d": 
		if move("right"):
			add_block()
	if userInput is "w": 
		if move("up"):
			add_block()

