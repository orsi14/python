import engine
import random 

# the agent contains the logic to make decisions on what move to make

def make_move(game, type='random'):

	if type == 'minDerivative':
		myMatrix = {}
		for direction in game.moves:
			myMatrix[direction] = game.calculate_move(game.matrix,direction)
		
	else:
		# randomly pick a move
		myMove = random.choice(game.moves)
		#print(myMove)
		while game.move(myMove) is False:
			myMove = random.choice(game.moves)

	return game


