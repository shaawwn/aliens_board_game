# Main file to run aliens simulation including the main simulation class and methods
import marines_aliens as ma 
import movement_functions as mf 
from random import choice, randint
#import game_board


class AliensSimulation:
	"""Main class containing Aliens Board game simulation methods"""

	def __init__(self):
		"""Sim attributes if any"""
		self.game_state = True
		self.game_start = True
		self.marines_spawn = False
		self.count = 0
		self.aliens = []
		self.marines = self.marines_list()
		self.marine_coordinates = [] # This needs to empty and update every turn
		self.game_board = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
			['E', 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
			[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]]


	def print_board(self, board):
		"""Print out the game board"""
		for row in board:
			print(row)


	def marines_list(self):
		"""Create marines and put them into a list"""
		pistol = ma.Weapon("Pistol", (5, 6), [[2, 1, 0], [6,2,1,0]])
		apone_flame = ma.Weapon("Flame Unit", (3, 4), [[8,6,4], [14,13,9], [15,14,10]])
		hicks_shotgun = ma.Weapon("Shotgun", 7, [[8,6,2,1,0], [13,9,8,6,4], [14,10,9,7,5]])
		machine_gun = ma.Weapon("Machine Gun", 7, [[8,6,3,2,1], [13,9,8,7,6]])
		flame_unit = ma.Weapon("Flame Unit", (3, 4), [[7,5,3], [13,9,8]])

		marines ={
			'apone': [(3, 1), apone_flame], 
			'hicks': [(3, 1), hicks_shotgun],
			'drake': [(2, 1), machine_gun],
			'vasquez': [(2, 1), machine_gun],
			'dietrich': [(2, 0), flame_unit],
			'wierzbowski': [(2, 0), flame_unit],
			'frost': [(2, 0), pistol], 
			'crowe': [(2, 0), pistol],
			'hudson': [(2, 0), pistol],
			}

		marines_list = []
		weapon_range = [1, 2, (3, 4), (5, 6), 7]
		for keys, values in marines.items():
			keys = ma.Marine(keys,values[0][0], values[0][1], values[1])
			marines_list.append(keys)
		return marines_list



	def main_loop(self):
		"""Populate the game board with randomly spawning aliens
		and marines from the marines list"""
		turn_counter = 0 # check how many turns before loop breaks

		while self.game_state:
			# Spawn marines into game board
			self.spawn_marines()

			# Spawn aliens into game board
			self.spawn_aliens()

			# Alien turn
			self.alien_turn()
			turn_counter += 1

			# Print out game board and end loop if number of aliens >10
			#self.print_board(self.game_board) #Prints out a gameboard each turn
			print('\n')

			# Print tests to check marine/alien values
			# Alien coordinates and status
			for alien in self.aliens:
				print(f"{alien.coordinates}: {alien.status}")
			# Marine coordinates, status, current weapon
			for marine in self.marines:
				print(f"{marine.name}: {marine.coordinates}")
				if marine.status != "normal":
					print(f"{marine.name}: {marine.status}: {marine.weapon.weapon_name}")

			# Temporary break conditions for the while loop
			if len(self.aliens) >= 10:
				self.game_state = False
			if len(self.marines) < 0:
				self.game_state = False


	def alien_turn(self):
		"""Manage the alien turn during the game round
		Move aliens. If they move 4 spaces, go to the next alien.  If they
		find a marine, fight the marine, set marine/alien status."""
		for alien in self.aliens:
			for n in range(alien.actions):

				alien.range = mf.piece_range(mf.true_range(alien.actions), alien.coordinates)
				self.game_board[alien.coordinates[0]][alien.coordinates[1]] = 0
				mf.movement(self.game_board, n, alien)

				self._check_square(alien) # check if the alien is in the same square as an alien
				#Fight marine/alien
				if self._check_square(alien) == True:
					self.alien_fight_marine(alien)
					# resolve the outcome of the fight
					# set gameboard accordingly
					#self.game_state = False
					break
				else:
					self.game_board[alien.coordinates[0]][alien.coordinates[1]] = alien.game_piece



	def spawn_marines(self):
		"""Spawn marines onto the game board"""
		if self.marines_spawn == False:
			for marine in self.marines:
				mf.get_marine_coordinates(self.game_board, marine)
				a = marine.coordinates[0]
				b = marine.coordinates[1]
				self.marine_coordinates.append([a, b])
				self.game_board[a][b] = marine.game_piece
			self.marines_spawn = True


	def spawn_aliens(self):
		"""Spawn new aliens for each game round, starting with 4 at the
		start of the game, then 2 for each subsequent game round"""
		if self.game_start == True:
			alien_spawn = 4
			self.game_start = False
		else:
			alien_spawn = 2
		for alien in range(alien_spawn):
			alien = ma.Alien()
			self.aliens.append(alien)
			mf.spawn_alien(self.game_board, alien)
			self._check_square(alien) # Checks if an alien is in same spot as marine
		

	def _check_square(self, alien):
		"""Check if an alien spawns or moves onto a square with a marine"""
		x = alien.coordinates[0]
		y = alien.coordinates[1]
		if [x, y] in self.marine_coordinates:
			return True
		else:
			self.game_board[x][y] = alien.game_piece

	def alien_fight_marine(self, alien):
		"""The alien fights a marine if they occupy the same game space"""
		x = alien.coordinates[0]
		y = alien.coordinates[1]
		if [x, y] in self.marine_coordinates:
			for marine in self.marines:
				if marine.coordinates == (x, y):
					self.game_board[x][y] = [alien, marine]
					self.update_marine_alien_status(marine, alien)
					self.determine_outcome(alien, marine)
					# Print out Marine/Alien status to check
					print(f"Marine: {marine.status}")
					print(f"alien: {alien.status}")


	def determine_outcome(self, alien, marine):
		"""After the alien and marine fight, determine the ooutcome 
		on the game board of the fight"""
		print("Checking determine outcome")
		if marine.status == 'killed':
			self.marines.remove(marine)
			alien.status = 'normal'

		if alien.status == "stunned":
			"""Move alien to nearest adjacent square, it loses a turn
			Uncomment print() to check alien coordinates before
			and after"""
			#print(f"Stunned coord1 = {alien.coordinates}")
			mf.movement(self.game_board, 1, alien)
			#print(f"New coordinates = {alien.coordinates}")

		elif marine.status == 'incapacitated and grabbed':
			alien.holding_counter = 1
			marine.incapacitated()
			# set marine stats to inc (no actions)
			# Set alien stats to grabbing, set a counter to 1, and increment
				# -1 on next turn.  If 0, remove both alien and marine

		elif marine.status == 'wounded and grabbed':
			"""Set marine status to wounded, alien status is set to 'holding marine',
			remove both alien and marine on the next turn if alien is not killed during
			marine turn"""

			# Wounded statistics for weapons, need to simplify this
			wound_pistol = ma.Weapon("Wound Pistol", (2, 3), [[0], [4, 0]])
			wound_apone = ma.Weapon("Wound Flame Unit", (3, 4), [[5,3,1], [11,10,6], [12,11,7]])
			wound_machine = ma.Weapon("Wound Machine Gun", 7, [[5,3,0], [10,6,5,4,3]])
			wound_flame = ma.Weapon("Wound Flame Unit", (3,4), [[4,2,0], [10,6,5]])
			wound_hicks = ma.Weapon("Wound Shotgun", 7, [[5,3],[10,6,5,3,1], [11,7,6,4,2]])

			alien.holding_counter = 1 # On the next turn, decrement to 0
			if marine.name in ['hudson', 'frost', 'crowe']:
				marine.weapon = wound_pistol
			elif marine.name in ['wierzbowski', 'dietrich']:
				marine.weapon = wound_flame
			elif marine.name == 'apone':
				marine_weapon = wound_apone
			elif marine.name in ['drake', 'vasquez']:
				marine.weapon = wound_machine
			elif marine.name == 'hicks':
				marine.weapon = wound_hicks
		elif marine.status == 'in combat':
			'''Marine and alien remain in combat, marine does not get a turn,
			alien does not move, and each turn only resolve alien turn combat'''
			marine.actions = 0
			alien.actions =0


	# Make a function for if aliens and marines are on the same spot....
	def alien_attack_roll(self, marine, alien):
		"""Roll a 10-sided die and check against alien attack roll values, adding in
		the melee value for the marine on top of the roll"""
		attack_roll = randint(0, 9) + marine.melee
		if attack_roll > 9:
			attack_roll = 9
		for value in alien.attack_rolls:
			if attack_roll in value:
				return alien.damage_table[value]


	def update_marine_alien_status(self, marine, alien):
		"""Update the alien and marine status using the outcome of the alien attack
		roll which is then put into the aliens attack table to get a status outcome.
		Format is (marine, alien) for status"""
		outcome = self.alien_attack_roll(marine, alien)
		marine.status = outcome[0]
		alien.status = outcome[1]
		return (marine.status, alien.status, outcome)





test = AliensSimulation()
test.main_loop()



# ---------------------------- TO ADD/NOTES/TESTING ----------------------


def marine_attack_roll(marine, aim, alien):
	"""Marines attack rolls using a 10-sided die (range 0-9), using the marines
	equipped weapon stats. Aim value is used in the weapons damage table as the key
	and checks if the 10-sided roll outcome results in a hit or not."""
	attack_roll = randint(0, 9)
	if attack_roll <= max(marine.weapon.aim_table[aim]): # Max used here because any roll less than the max is a hit
		aliens.remove(alien)
		print("Alien killed")
	else:
		print("The shot missed")

def marine_combat(marine, aim, alien):
	""" Determine the outcome of a marines attack on an alien"""
	return

# Choose a marine and have them attack
def simple_game_round():
	"""Simplified game round to test marine/alien methods and attributes"""
	alien_targets = marines_list[:]
	for alien in aliens: # Need to make adjustments so they don't choose the same marines
		marine = choice(alien_targets)
		alien_targets.remove(marine)
		update_marine_alien_status(marine, alien)
		print(marine.status, alien.status)

	for marine in marines_list:
		if marine.status == "normal":
			if len(aliens) < 1:
				print("All the aliens are dead")
				break
			alien = choice(aliens)
			marine_attack_roll(marine, 2, alien)

		elif marine.status == "in combat":
			print("This marine can only melee")
		else:
			print("Marine is incapable of attacking")

	print(len(aliens))
	for marine in marines_list:
		if marine.status == "normal":
			print(marine.name.title())
		else:
			print(f"{marine.name.title()} is {marine.status}")




