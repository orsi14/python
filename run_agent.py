import engine 
import agent
import logging

# Define constants
# row and col define how many rows and columns are in the matrix
logging.basicConfig(filename='agent.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
game_size = 4
methods = ['random','minDerivative']
agent_method = 'minDerivative'

for x in range(1):
	# Initialize game
	myGame = engine.Game(4)
	myGame.add_block()

	# Format of matrix is:
	# matrix[row id,col id]
	# where 0,0 is the top left


	while myGame.is_move_possible():
		#myGame.print_matrix(False)
		agent.make_move(myGame, agent_method)
		myGame.add_block()
	x += 1

	logging.info('Method:%s; Max:%d; Total:%d', agent_method, myGame.matrix.max(), myGame.matrix.sum())