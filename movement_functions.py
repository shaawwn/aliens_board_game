# Movement functions for navigating game board in Aliens board game simulation
from random import choice, randint
from time import sleep
import marines_aliens as ma

def print_board(board):
	"""Print out a 2d array for visual purposes"""
	for row in board:
		print(row)

# ---------------------------------- SPAWNING FUNCTIONS -----------------------


# -----------------ALIENS ---------------------

def get_alien_coordinates(board):
	"""Get coordinates for alien random spawns"""
	row = randint(0, len(board) - 1)
	column = randint(0, len(board[0]) - 1)
	return row, column


def spawn_alien(board, game_piece):
	"""Spawn alien into game board, commented out portions test they
	don't spawn in illegal locations: 1 or 'A', however they may spawn
	on a Marine"""

	game_piece.coordinates = get_alien_coordinates(board)
	while board[game_piece.coordinates[0]][game_piece.coordinates[1]] == 1 or board[game_piece.coordinates[0]][game_piece.coordinates[1]] == 'A':
		#if board[game_piece.coordinates[0]][game_piece.coordinates[1]] == 'A':
		#	print("Aliens on same spot")
		#	print(f"Same spot coordinates: {game_piece.coordinates}")
		#elif board[game_piece.coordinates[0]][game_piece.coordinates[1]] == 1:
		#	print("Spawned on a 1")
		game_piece.coordinates = get_alien_coordinates(board)
			# If coordinates are the same as a marine, create a list containing the marine and alien
		if board[game_piece.coordinates[0]][game_piece.coordinates[1]] == 'M':
			board[game_piece.coordinates[0]][game_piece.coordinates[1]] == [game_piece.game_piece, 'M']
		#print(f": New coordinates: {game_piece.coordinates}")


# -----------------MARINES -------------------

def get_marine_loc(board):
	"""Marines have a limited spawn area compared to aliens, this returns 
	coordinates that are valid per the game rules for marine starting spawns"""
	row = randint(0, len(board) - 1)
	column = randint(17, len(board[0]) - 1)
	return row, column


def get_marine_coordinates(board, marine):
	"""Spawn the marines on the right side of the map"""
	# Start from index 17 to 24 on game board.
	marine.coordinates = get_marine_loc(board)
	while board[marine.coordinates[0]][marine.coordinates[1]] != 0:
		marine.coordinates = get_marine_loc(board) 



# --------------------------- MOVEMENT FUNCTIONS ----------------------------

def move(i, board, free_move=True): # Modified to include no border game board
	"""Directions for moving a game piece a single space, where
	free_move is a game piece that is unobstructed in all directions"""
	direction = [-1, 0, 1]
	n = 0
	x = 0 
	if i == 0:
		n = choice([0, 1])
	elif i >= len(board) - 1:
		n = choice([-1, 0])
	if free_move == True: 
		n = choice(direction)
	return n


def last_movement(i, j, board):
	"""If an alien has only 1 movement left, makes sure it will land on 
	only a legal to occupy space: 0, or 'M'"""
	n = move(i, board)
	m = 0
	while last_legal_hori_move(i, j, n, board) == False:
		i_move = move(i, board)
		n = i_move

	m = move(j, board)
	while last_legal_vert_move(i, j, m, board) == False:
		j_move = move(j, board[i])
		m = j_move
	return n, m


def last_legal_vert_move(i, j, n, board):
	"""Check for a valid vertical move on an aliens last movement"""
	#print("Last legal Vert move")
	if j + n > len(board[i]) - 1 or board[i][j + n] == 1 or board[i][j + n] == 'A' or j + n < 0:
		return False
	else:
		return True


def last_legal_hori_move(i, j, n, board):
	"""Check for a valid horizontal move on an aliens last movement"""
	#print("last legal hori movie")
	if i + n > len(board) - 1 or board[i + n][j] == 1 or board[i + n][j] == 'A' or i + n < 0:
		return False
	else:
		return True


def advanced_directions(i, j, board): 
	"""Advanced directions for moving a game piece across the game board
	Moves a piece in i and j directions ,where (i, j) is equivalent to (x, y)
	Returns new coordinate values for game piece
	"""
	n = move(i, board)
	m = 0
	# Check for a valid move
	while check_legal_hori_moves(i, j, n, board) == False:
		#print("Stuck in while loop for hori")
		i_move = move(i, board, free_move=False)
		n = i_move

	m = move(j, board[i])
	# Check for a valid move
	while check_legal_vert_moves(i, j, m, board) == False:
		j_move = move(j, board[i], free_move=False)
		m = j_move

	return n, m
# Changed from !=0 to == 1

# If moves == 1, then an alien may only move into a 0, or an 'M' space.
def check_legal_vert_moves(i, j, n, board):
	"""Checks that verticle moves are legal"""
	if j + n > len(board[i]) - 1 or board[i][j + n] == 1 or j + n < 0:# or j + n >= len(board[i]):
		return False
	else:
		return True


def check_legal_hori_moves(i, j, n, board):
	"""Checks the legality of a game piece move, returns boolean"""
	if i + n > len(board) - 1 or board[i + n][j] == 1 or i + n < 0: # or i + n >= len(board) - 1:
		return False
	else:
		return True


def check_marine_move():
	"""Allow for movement THROUGH other marines, but otherwise obstacles,
	boundaries, and aliens are still not legal.  Moving in directions i or j to
	be considered ONE move, not (i, j)"""
	# TODO
	return


def check_alien_move():
	"""Allow for movement THROUGH other aliens and ONTO marine squares. Need a function
	to create an alien/marine list so that two game pieces can occupy same spot on the board.
	Obstacles, boundaries still illegal, and moving in directions i or j to be ONE move, 
	not(i, j)"""
	# TODO
	return


def choose_direction(i, j):
	"""Choose a direction for a movement, either horizontal
	or vertical, (i, j) accordingly"""
	direction = choice([i, j])
	if direction == i:
		i += i
		return i, j
	elif direction == j:
		j += j
		return i, j


def check_space():
	# Obsolete/No need
	"""During movement, check if a space is already occupied"""
	if board[i][j] == 'M':
		print("Same spot!!!")
		board[i][j] = [game_piece.game_piece, 'M']
	else:
		board[i][j] = game_piece.game_piece
	return


def movement(board, moves, game_piece):
	"""Returns a single move for a game piece, use in a loop for multiple
	moves using game_piece actions as movement"""

	if game_piece.status == 'just spawned':
		moves = 1
		game_piece.status = 'normal'

	i = game_piece.coordinates[0]
	j = game_piece.coordinates[1]

	if moves == game_piece.actions - 1: # The final movement
		directions = last_movement(i, j, board)
	else:
		directions = advanced_directions(i, j, board)

	# Choose direction
	direction = choice([i, j]) # Decides what direction to move
	if direction == i:
		i += directions[0]
	elif direction == j:
		j += directions[1]
	game_piece.coordinates = i, j
	#Game piece range function here maybe?
	sleep(0.0) # Set a value to check game board during loop
	

def move_piece(board, moves, game_piece):
	# Older function that got changed to movement() simplified
	"""Simulates a game piece moving across a game board with movement
	functions.  Cursor is game piece, optional sleep method to make
	observing game movements easier"""# Modified from previous adv. board nav. below
	
	# For new aliens, set movement to 1 space, and set status to normal
	if game_piece.status == 'just spawned':
		moves = 1
		game_piece.status = 'normal'


	# If random coordinates are not legal moves, repeat get_coordinates() until
		# legal coordinates 

	i = game_piece.coordinates[0]
	j = game_piece.coordinates[1]
	for n in range(moves):
		print_board(board) ########## Removed just to test
		board[i][j] = 0
		if n == moves - 1: # When an alien only has 1 movement left,cannot occupy same space as another alien
			piece_directions = last_movement(i, j, board)
		else: 
			piece_directions = advanced_directions(i, j, board)

		# Return i OR j, x OR y
		direction = choice([i, j])
		if direction == i:
			i += piece_directions[0]
		elif direction == j:
			j += piece_directions[1]

		# Check that a marine is in a space, if so, both alien and marine will occupy same spot, else place the game piece at coordinates
		if board[i][j] == 'M':
			print("Same spot!!!")
			board[i][j] = [game_piece.game_piece, 'M']
		else:
			board[i][j] = game_piece.game_piece # add .game_piece to better visualize

		game_piece.coordinates = i, j
		game_piece.range = piece_range(true_range(moves), game_piece.coordinates)

		sleep(0.5)





# ---------------------- RANGE FUNCTIONS ------------------

# Functions for finding movement/firing range for aliens and marines

def true_range(range_area):
	"""Return values to be used in range() based on given range
	Note: Range value needs is + 1 to the actual desired range"""
	neg_range = range_area * -1
	pos_range = range_area + 1
	true_range = (neg_range, pos_range)
	return range(neg_range, pos_range)#true_range


def piece_range(distance_range, cursor_index):
	"""Find the range for a game piece, distance_range = return 
	value for true_range(), cursor_index = game_piece.coordinates"""
	range_index = []
	n = distance_range[0]
	for i in distance_range:
		#print(f"{i}: i value")
		if i < 1:
			j_range = n - i
		#	print(f"{j_range}: j range value")
		elif i > 0:
			j_range = n + i
		ax = cursor_index[0]
		ax += i # Starts at -3 for range of 4, j then gets the remaining 1 '1'
		
		j_distance_range = range(j_range, -j_range + 1)
		#print(f"{j_distance_range}: j range")
		for j in j_distance_range:
			x_y = []
			ay = cursor_index[1]
			ay += j
			x_y.append(ax)
			x_y.append(ay)
			range_index.append(x_y)
	return range_index

# -------------------------------- TESTING FUNCTIONS ----------------------------

def check_one(board):
	"""Checks for the number of obstacles in the game board, where '1' is
	and obstacle"""
	counter = 0 
	for row in board:
		for item in row:
			if item == 1:
				counter += 1
	return counter