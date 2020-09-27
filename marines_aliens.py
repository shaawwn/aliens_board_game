from random import randint


# Marine, Weapon, and Alien classes.  
# Try and add parent class for attributs shared between classes

# ------------------GAME PIECES CLASS ---------------------------

# Parent class for Marines and Aliens

class GamePiece:
	"""WIP Parent class for Aliens and Marines"""

	def __init__(self):
		"""Initialize game piece attributes"""
		self.status = None
		self.coordinates = None
		self.actions = None


# ---------------MARINE AND WEAPON CLASSES-----------------------
class Marine:
	"""The space marines in the Aliens board game"""

	def __init__(self, name, AP, melee, weapon, status='normal'):
		"""Initialize the Marine attributes"""
		self.name = name
		self.AP = AP
		self.backup_AP = AP
		self.melee = melee
		self.weapon = weapon
		self.status = status
		self.game_piece = 'M'
		self.coordinates = None

	
	def incapacitated(self):
		"""If a marine is grabbed by an alien, reduce marine Action Point(AP)
		to zero"""
		if self.status == 'incapacitated and grabbed': # or grabbed
			self.AP = 0
		else:
			self.AP = self.backup_AP

	
	# Probably remove later, but keep now just in case
	def wounded(self, wounded_weapon):
		"""Wound the marine if it is either wounded, change the weapon to
		wounded status weapon use"""
		self.weapon = wounded_weapon


	# TODO Functions
	def attributes(self):
		return f"Name: {self.name.title()}, AP: {self.AP}, Melee: {self.melee} "#Weapon: {self.weapon.title()}"

	def move_marine(self):
		return f"{self.name.title()} moves  1 space up, and 1 space to the left"

	def display_weapons(self):
		"""Display marine weapon stats"""
		return self.weapon.display_stats()

	# Returns marines weapon table
	def display_aim_table(self):
		"""Displays the marine's held weapon aim table."""
		return self.weapon.create_aim_table()



class Weapon:
	"""Weapons used by the marines during the game"""

	def __init__(self, weapon_name, weapon_range, aim):
		"""Initialize the marines' weapon attributes"""
		self.weapon_name = weapon_name
		self.weapon_range = weapon_range
		self.aim = aim
		self.aim_table = self.create_aim_table()



	def display_stats(self):
		"""Display weapon attributes"""
		return f"Weapon: {self.weapon_name}, Range: {self.weapon_range}, Aim: {self.aim}"

	
	def create_weapon_range(self):
		"""Using the given range, takes the value given and creates attack 
		roll values up to and including the given range, ie '7' will include 
		all value, (3, 4) will only include range values up to (3, 4)"""
		weapon_range = []
		if self.weapon_range == 7:
			weapon_range = [1, 2, (3, 4), (5, 6), 7]
		elif self.weapon_range == (5, 6):
			weapon_range = [1, 2, (3, 4), (5, 6)]
		elif self.weapon_range == (3, 4):
			weapon_range = [1, 2, (3, 4)]
		self.weapon_range = weapon_range
		return self.weapon_range


	def create_aim_table(self):
		"""Using the given Aim, and an expanded weapon range, create the weapons
		damage table.  This returns a dictionary that uses the AIM value as a key
		and the dice roll requirements as values"""
		aim_table = {}
		for i in range(len(self.aim)):
			aim_table[i + 1] = self.aim[i]
		return aim_table


# ---------------------------ALIEN CLASS-------------------------------

class Alien:
	"""Class for managing creation of new aliens and alien stats and
	abilities"""
	def __init__(self, status=None):
		"""Initializes attributes for the aliens. Status default is None, but
		can be changed during main loop"""
		self.status = status
		self.actions = 4
		self.attack_rolls = [(0,), (1, 2), (3, 4), (5, 6), (7, 8), (9,)]
		self.damage_table = self.attack_table()
		self.game_piece = 'A'
		self.coordinates = None
		self.range = None
		self.holding_counter = None


	# Main file handles spawning aliens, so probably delete this later
	def spawn_alien(self):
		"""On every turn, spawn two aliens who have a 1 move limitation"""
		self.status = 'just spawned'
		return "A new alien spawns and moves 1 space"


	# Main file handles status changes so probably delete later
	def old_alien(self):
		"""For aliens that spawned the previous turn, change status to "normal"""
		if self.status == 'just spawned':
			self.status = 'normal'
		return 'This alien can move 4 spaces'


	def attack_table(self):
		"""Creates the outcome table for alien attack rolls as a dictionary. Key
		is the attack roll outcome, values are status outcomes for rolls in 
		(marine, alien) format."""
		table = {(0,): ("killed", "normal"),
				(1, 2): ("incapacitated and grabbed", "holding marine"),
				(3, 4): ("wounded and grabbed", "holding marine"),
				(5, 6): ("grabbed", "holding marine"),
				(7, 8): ("in combat", "in combat"),
				(9,): ("normal", "stunned"),
				}
		return table



