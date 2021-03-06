from random import *
from numpy import *
import logging

class Game:
	# game parameters
	probability_of_four = 0.15 # this is the probability that a new block will be a 4
	moves = ['up', 'down', 'left', 'right']

	def __init__(self, game_size):
		self.matrix = zeros(shape=(game_size,game_size))
		self.game_size = game_size

	def print_matrix(self, pretty_print=True):

		for a in range(len(self.matrix)):
			print("|", end=' ')
			for b in range(len(self.matrix)):
				value = int(self.matrix[a,b]) if self.matrix[a,b] > 0 else ''
				print(value, "\t|", end=' ')
			if pretty_print:
				print()
		print
	
	@staticmethod 
	def calculate_derivative(matrix)
		# return square of derivative
		sumOfSquares = square(gradient(matrix)[1]).sum()
		
		print(matrix)
		print(sumOfSquares)
		
		

	# This is a static class so that it can be used to calculate what the move would look like without updating the matrix object in the class
	@staticmethod
	def calculate_move(matrix, direction="left"):
		# ToDo: sanitize the arguments so that the function handles invalid direction inputs

		# define a bunch of values for each direction of motion
		directionLookup = {"left": [-1,1,len(matrix)-1,1], "right": [1,len(matrix)-2,0,-1], "up": [-1,1,len(matrix)-1,1], "down": [1,len(matrix)-2,0,-1]}
		
		if direction is "up" or direction is "down":
			matrix = matrix.transpose()
			
		dirCol = directionLookup[direction][0]
		startCol = directionLookup[direction][1]
		endCol = directionLookup[direction][2]
		stepDir = directionLookup[direction][3]
		
		# for each row, start from the second from the left and move it as far left as possible
		# then move to the next cell and do the same
		hasMoved = False
		
		#go through every row (arow will be 0,1,2,3)
		for arow in range(len(matrix)):
			#within each row, go through each column (1,2,3) or (2,1,0), either left to right or right to left
			for acol in range(startCol,endCol+stepDir,stepDir):
					
				# the first thing we're going to do is combine any cells that should be combined (same value as the cell next to it)
				# constraint is that only 2 cells can be merged together, no double merging or multi-step merging
				
				#if the box is not empty - if it's empty we dont care about moving anything in it
				if matrix[arow,acol] > 0:
					# in this block, we've found a number.  
					# start looking in the previous cell, which has index of checkCol
					checkCol = acol+dirCol
					
					#print("Found a thing to move. It's value is '",matrix[arow,acol],"'",)
					#print("Box of interest at (", arow, ",",acol, ") is ", matrix[arow,acol])
					#print("To its", direction, "has a value of ", matrix[arow,checkCol])
					
					# keep moving the cell until we hit the end of find a non-empty cell
					while checkCol >= 0 and checkCol < len(matrix) and matrix[arow,checkCol] == 0:
						
						# if we move the cell, register that we moved it so we know to add a new box
						hasMoved = True
						
						#print("Empty box at (", arow, ",",checkCol,") is ", matrix[arow,checkCol])
						#print("Putting value ", matrix[arow,checkCol+stepDir], "into it")
											
						matrix[arow,checkCol] = matrix[arow,checkCol+stepDir]
						matrix[arow,checkCol+stepDir] = 0
						checkCol -= stepDir
						#print_matrix()
		
		for arow in range(len(matrix)):
			for b in range(startCol+dirCol,endCol,stepDir):
				# if the cell to the right is the same, squish em together
				# and then move all other cells one to the left
				if matrix[arow,b] == matrix[arow,b+stepDir] and matrix[arow,b] > 0:
					
					# print("We're looking at cell",arow,b,"in this matrix and comparing it to:",arow,b+stepDir)
					hasMoved = True
					# print("Value of both cells is:",matrix[arow,b],"We'll be assigning a value of:",2*int(matrix[arow,b]))
					# print(matrix)
					
					matrix[arow,b] = 2 * int(matrix[arow,b])
					
					# print("We've just set the value to:", matrix[arow,b])
					matrix[arow,b+stepDir] = 0
					moveCol = b+stepDir
					while moveCol < len(matrix)-stepDir and moveCol > 0:
						matrix[arow,moveCol] = matrix[arow,moveCol+stepDir]
						matrix[arow,moveCol+stepDir] = 0
						moveCol += stepDir
		
		if direction is "up" or direction is "down":
			matrix = matrix.transpose()
		
		return {'matrix':matrix, 'hasMoved':hasMoved}
	
	def move(self, direction="left"):
		result = self.calculate_move(self.matrix, direction)
		self.matrix = result['matrix']
		return result['hasMoved']
	
	
	def is_move_possible(self):
		move_possible = True
		# ToDo - refactor to make this cleaner
		if count_nonzero(self.matrix) >= len(self.matrix)**2: 
			# print("Game is full")
			move_possible = False
			# if all of the blocks are non-zero, see if there is a possible move
			for arow in range(len(self.matrix)-1):
				for acol in range(len(self.matrix)-1):
					#go through every cell, excluding the last row and column and check if the cell
					#next to it or below it is the same
					if self.matrix[arow,acol] == self.matrix[arow+1,acol] or self.matrix[arow,acol] == self.matrix[arow,acol+1]:
						# print("Found a possible move looking at",arow,acol)
						move_possible = True
			# check last row and column
			for acol in range(len(self.matrix)-1):
				if self.matrix[len(self.matrix)-1][acol] == self.matrix[len(self.matrix)-1][acol+1]:
					move_possible = True
				
			for arow in range(len(self.matrix)-1):
				if self.matrix[arow][len(self.matrix)-1] == self.matrix[arow+1][len(self.matrix)-1]:
					move_possible = True
					
		return move_possible
		
	def add_block(self):

		# print("We are about to add a block to this matrix:")
		# print_matrix()
		
		# pick a random block value - some percentage of time it will be 4
		value = int((randrange(0,100)<(100*Game.probability_of_four))*2 + 2)
		
		foundEmpty = False
		# pick a random coordinate and see if it is empty
		while not foundEmpty: 
			newRow = randrange(len(self.matrix))
			newCol = randrange(len(self.matrix))
			if self.matrix[newRow,newCol] == 0:
				foundEmpty = True
				self.matrix[newRow,newCol] = value
				